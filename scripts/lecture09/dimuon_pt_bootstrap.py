#!/usr/bin/env python
"""Fit CMS dimuon mass spectra in one pT bin and bootstrap the fitted parameters.

This script is intended for Lecture 9 batch jobs.  Each Slurm job should run one
dimuon pT selection, write one CSV file, and then the lecture notebook can collect
the CSV files from all completed bins.
"""

from __future__ import annotations

import argparse
import os
from datetime import datetime
from pathlib import Path
from time import perf_counter

import numpy as np
import pandas as pd
from scipy.optimize import minimize
from scipy.special import erf


MASS_COLUMN = "dimuon_mass_GeV"
PT_COLUMN = "dimuon_pt_GeV"
DEFAULT_MASS_RANGE = (2.6, 3.6)


def log(message):
    """Print one timestamped diagnostic line for Slurm stdout."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{timestamp}] {message}", flush=True)


def normal_cdf(x, mean, sigma):
    """Evaluate the Gaussian cumulative distribution function."""
    return 0.5 * (1.0 + erf((x - mean) / (np.sqrt(2.0) * sigma)))


def truncated_gaussian_pdf(x, mean, sigma, lower, upper):
    """Gaussian PDF normalized inside [lower, upper]."""
    normalization = normal_cdf(upper, mean, sigma) - normal_cdf(lower, mean, sigma)
    density = np.exp(-0.5 * ((x - mean) / sigma) ** 2) / (np.sqrt(2.0 * np.pi) * sigma)
    return density / normalization


def truncated_exponential_pdf(x, slope, lower, upper):
    """Exponential PDF normalized inside [lower, upper]."""
    width = upper - lower
    if abs(slope) < 1.0e-10:
        return np.ones_like(x, dtype=float) / width
    normalization = (1.0 - np.exp(-slope * width)) / slope
    return np.exp(-slope * (x - lower)) / normalization


def unpack_parameters(transformed_parameters):
    """Convert optimizer parameters into physical parameters."""
    log_signal_yield, log_background_yield, mass_mean, log_mass_sigma, log_mass_slope = transformed_parameters
    return {
        "signal_yield": float(np.exp(log_signal_yield)),
        "background_yield": float(np.exp(log_background_yield)),
        "mass_mean_GeV": float(mass_mean),
        "mass_sigma_GeV": float(np.exp(log_mass_sigma)),
        "background_mass_slope": float(np.exp(log_mass_slope)),
    }


def initial_parameters(n_events):
    """Choose stable starting values for the selected pT bin."""
    signal_start = max(5.0, 0.55 * n_events)
    background_start = max(5.0, 0.45 * n_events)
    return np.array(
        [
            np.log(signal_start),
            np.log(background_start),
            3.09,
            np.log(0.035),
            np.log(0.7),
        ]
    )


def parameter_bounds(n_events):
    """Bounds for transformed optimizer parameters."""
    yield_upper = max(100.0, 5.0 * n_events)
    return [
        (np.log(1.0e-3), np.log(yield_upper)),
        (np.log(1.0e-3), np.log(yield_upper)),
        (3.0, 3.2),
        (np.log(0.010), np.log(0.20)),
        (np.log(0.001), np.log(20.0)),
    ]


def full_intensity(mass_values, transformed_parameters, mass_range):
    """Evaluate the signal-plus-background event intensity."""
    lower, upper = mass_range
    parameters = unpack_parameters(transformed_parameters)
    signal = truncated_gaussian_pdf(
        mass_values,
        parameters["mass_mean_GeV"],
        parameters["mass_sigma_GeV"],
        lower,
        upper,
    )
    background = truncated_exponential_pdf(
        mass_values,
        parameters["background_mass_slope"],
        lower,
        upper,
    )
    return parameters["signal_yield"] * signal + parameters["background_yield"] * background


def negative_log_likelihood(transformed_parameters, mass_values, mass_range):
    """Extended unbinned negative log-likelihood for the mass model."""
    parameters = unpack_parameters(transformed_parameters)
    lower, upper = mass_range

    if not (lower < parameters["mass_mean_GeV"] < upper):
        return 1.0e30
    if not (0.005 < parameters["mass_sigma_GeV"] < 0.30):
        return 1.0e30

    event_intensity = full_intensity(mass_values, transformed_parameters, mass_range)
    if np.any(event_intensity <= 0.0) or np.any(~np.isfinite(event_intensity)):
        return 1.0e30

    n_model = parameters["signal_yield"] + parameters["background_yield"]
    return n_model - np.sum(np.log(event_intensity))


def fit_mass_model(mass_values, mass_range, starting_point=None):
    """Fit the signal-plus-background mass model for one selected dataset."""
    if starting_point is None:
        starting_point = initial_parameters(len(mass_values))
    return minimize(
        negative_log_likelihood,
        x0=starting_point,
        args=(mass_values, mass_range),
        method="L-BFGS-B",
        bounds=parameter_bounds(len(mass_values)),
        options={"maxiter": 20000, "ftol": 1.0e-9},
    )


def bootstrap_fit_rows(mass_values, mass_range, n_bootstrap, rng, pt_min, pt_max, starting_point):
    """Resample selected events with replacement and refit each bootstrap sample."""
    rows = []
    n_events = len(mass_values)
    n_success = 0
    progress_interval = max(1, min(25, n_bootstrap // 10))
    bootstrap_start = perf_counter()
    log(f"starting bootstrap loop with {n_bootstrap} resamples")
    for sample_index in range(n_bootstrap):
        sample_start = perf_counter()
        bootstrap_mass = rng.choice(mass_values, size=n_events, replace=True)
        fit_result = fit_mass_model(bootstrap_mass, mass_range, starting_point=starting_point)
        sample_elapsed = perf_counter() - sample_start
        row = {
            "sample_index": sample_index,
            "is_original_fit": False,
            "fit_success": bool(fit_result.success),
            "negative_log_likelihood": float(fit_result.fun),
            "pt_min_GeV": pt_min,
            "pt_max_GeV": pt_max,
            "n_events": n_events,
        }
        if fit_result.success:
            n_success += 1
            row.update(unpack_parameters(fit_result.x))
        rows.append(row)
        if (
            sample_index == 0
            or (sample_index + 1) % progress_interval == 0
            or sample_index + 1 == n_bootstrap
        ):
            elapsed = perf_counter() - bootstrap_start
            log(
                "bootstrap "
                f"{sample_index + 1}/{n_bootstrap}: "
                f"success={fit_result.success}, "
                f"sample_time={sample_elapsed:.2f} s, "
                f"elapsed={elapsed:.2f} s, "
                f"successful_fits={n_success}"
            )
    log(
        "finished bootstrap loop: "
        f"{n_success}/{n_bootstrap} fits succeeded in {perf_counter() - bootstrap_start:.2f} s"
    )
    return rows


def save_mass_fit_plot(mass_values, fit_parameters, mass_range, pt_min, pt_max, output_path, n_bins=50):
    """Save a diagnostic mass plot with histogram data and fitted model components."""
    os.environ.setdefault("MPLCONFIGDIR", f"/tmp/matplotlib-{os.environ.get('USER', 'user')}")
    import matplotlib

    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    lower, upper = mass_range
    bin_edges = np.linspace(lower, upper, n_bins + 1)
    bin_width = bin_edges[1] - bin_edges[0]
    mass_grid = np.linspace(lower, upper, 600)

    signal_density = truncated_gaussian_pdf(
        mass_grid,
        fit_parameters["mass_mean_GeV"],
        fit_parameters["mass_sigma_GeV"],
        lower,
        upper,
    )
    background_density = truncated_exponential_pdf(
        mass_grid,
        fit_parameters["background_mass_slope"],
        lower,
        upper,
    )
    signal_counts = fit_parameters["signal_yield"] * signal_density * bin_width
    background_counts = fit_parameters["background_yield"] * background_density * bin_width
    total_counts = signal_counts + background_counts

    fig, axis = plt.subplots(figsize=(8, 5))
    axis.hist(
        mass_values,
        bins=bin_edges,
        histtype="step",
        linewidth=1.8,
        color="black",
        label="Selected CMS dimuon data",
    )
    axis.plot(mass_grid, total_counts, color="tab:blue", linewidth=2.2, label="Total fit")
    axis.plot(mass_grid, signal_counts, color="tab:red", linestyle="--", linewidth=1.8, label="Signal")
    axis.plot(
        mass_grid,
        background_counts,
        color="tab:green",
        linestyle=":",
        linewidth=2.2,
        label="Background",
    )

    parameter_text = "\n".join(
        [
            rf"$p_T$ bin: [{pt_min:g}, {pt_max:g}) GeV",
            rf"$N_s$ = {fit_parameters['signal_yield']:.1f}",
            rf"$N_b$ = {fit_parameters['background_yield']:.1f}",
            rf"$\mu$ = {fit_parameters['mass_mean_GeV']:.5f} GeV",
            rf"$\sigma$ = {1000.0 * fit_parameters['mass_sigma_GeV']:.1f} MeV",
            rf"$\alpha_b$ = {fit_parameters['background_mass_slope']:.3f}",
        ]
    )
    axis.text(
        0.03,
        0.95,
        parameter_text,
        transform=axis.transAxes,
        va="top",
        ha="left",
        fontsize=10,
        bbox={"boxstyle": "round,pad=0.35", "facecolor": "white", "edgecolor": "0.75", "alpha": 0.9},
    )
    axis.set_title(r"CMS dimuon mass fit in one $p_T$ bin")
    axis.set_xlabel(r"$m_{\mu\mu}$ (GeV)")
    axis.set_ylabel(f"Events per {bin_width:.3f} GeV")
    axis.legend(loc="upper right", fontsize=9)
    axis.grid(alpha=0.25)
    fig.tight_layout()
    fig.savefig(output_path, dpi=180)
    plt.close(fig)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Run bootstrap mass fits for one CMS dimuon pT bin.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument("--data", type=Path, default=Path("data/cms_dimuon_jpsi_3000.csv"))
    parser.add_argument("--output-dir", type=Path, default=Path("slurm_outputs"))
    parser.add_argument("--pt-min", type=float, required=True, help="Lower dimuon pT edge in GeV.")
    parser.add_argument("--pt-max", type=float, required=True, help="Upper dimuon pT edge in GeV.")
    parser.add_argument("--n-bootstrap", type=int, default=200, help="Number of bootstrap refits.")
    parser.add_argument("--seed", type=int, default=20260924, help="Random-number seed.")
    parser.add_argument("--mass-min", type=float, default=DEFAULT_MASS_RANGE[0])
    parser.add_argument("--mass-max", type=float, default=DEFAULT_MASS_RANGE[1])
    parser.add_argument("--label", default=None, help="Optional output-file label.")
    return parser.parse_args()


def main():
    total_start = perf_counter()
    args = parse_args()
    mass_range = (args.mass_min, args.mass_max)
    rng = np.random.default_rng(args.seed)

    log("starting dimuon pT-bin bootstrap job")
    log(f"input data: {args.data}")
    log(f"output directory: {args.output_dir}")
    log(f"pT selection: {args.pt_min:g} <= {PT_COLUMN} < {args.pt_max:g} GeV")
    log(f"mass selection: {args.mass_min:g} <= {MASS_COLUMN} <= {args.mass_max:g} GeV")
    log(f"bootstrap resamples: {args.n_bootstrap}")
    log(f"random seed: {args.seed}")

    load_start = perf_counter()
    data = pd.read_csv(args.data)
    log(f"loaded {len(data)} rows in {perf_counter() - load_start:.2f} s")

    selection_start = perf_counter()
    selected = data[
        data[PT_COLUMN].ge(args.pt_min)
        & data[PT_COLUMN].lt(args.pt_max)
        & data[MASS_COLUMN].between(args.mass_min, args.mass_max, inclusive="both")
    ].copy()
    selection_elapsed = perf_counter() - selection_start
    log(f"selected {len(selected)} rows in {selection_elapsed:.2f} s")

    if len(selected) < 20:
        raise ValueError(
            f"Only {len(selected)} events selected for {args.pt_min} <= pT < {args.pt_max} GeV. "
            "Use wider pT bins or check the input data path."
        )

    mass_values = selected[MASS_COLUMN].to_numpy(dtype=float)
    log(
        "selected ranges: "
        f"mass=[{mass_values.min():.5f}, {mass_values.max():.5f}] GeV, "
        f"pT=[{selected[PT_COLUMN].min():.5f}, {selected[PT_COLUMN].max():.5f}] GeV"
    )
    log("starting original fit")
    fit_start = perf_counter()
    original_fit = fit_mass_model(mass_values, mass_range)
    fit_elapsed = perf_counter() - fit_start
    log(
        "original fit finished: "
        f"success={original_fit.success}, "
        f"nll={original_fit.fun:.6g}, "
        f"iterations={getattr(original_fit, 'nit', 'NA')}, "
        f"time={fit_elapsed:.2f} s"
    )
    original_row = {
        "sample_index": -1,
        "is_original_fit": True,
        "fit_success": bool(original_fit.success),
        "negative_log_likelihood": float(original_fit.fun),
        "pt_min_GeV": args.pt_min,
        "pt_max_GeV": args.pt_max,
        "n_events": len(selected),
    }
    if not original_fit.success:
        raise RuntimeError(f"Original fit failed: {original_fit.message}")
    original_row.update(unpack_parameters(original_fit.x))
    log(
        "original fit parameters: "
        f"signal_yield={original_row['signal_yield']:.3f}, "
        f"background_yield={original_row['background_yield']:.3f}, "
        f"mass_mean={original_row['mass_mean_GeV']:.6f} GeV, "
        f"mass_sigma={original_row['mass_sigma_GeV']:.6f} GeV, "
        f"background_slope={original_row['background_mass_slope']:.6f}"
    )

    rows = [original_row]
    rows.extend(
        bootstrap_fit_rows(
            mass_values,
            mass_range,
            args.n_bootstrap,
            rng,
            args.pt_min,
            args.pt_max,
            original_fit.x,
        )
    )

    write_start = perf_counter()
    args.output_dir.mkdir(parents=True, exist_ok=True)
    label = args.label
    if label is None:
        label = f"pt_{args.pt_min:g}_{args.pt_max:g}".replace(".", "p")
    output_path = args.output_dir / f"dimuon_bootstrap_{label}.csv"
    pd.DataFrame(rows).to_csv(output_path, index=False)
    log(f"wrote {len(rows)} rows to {output_path} in {perf_counter() - write_start:.2f} s")

    plot_start = perf_counter()
    plot_path = args.output_dir / f"dimuon_mass_fit_{label}.png"
    save_mass_fit_plot(
        mass_values,
        original_row,
        mass_range,
        args.pt_min,
        args.pt_max,
        plot_path,
    )
    log(f"wrote fit diagnostic plot to {plot_path} in {perf_counter() - plot_start:.2f} s")
    log(f"finished job in {perf_counter() - total_start:.2f} s")


if __name__ == "__main__":
    main()
