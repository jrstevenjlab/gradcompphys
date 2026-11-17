#!/usr/bin/env python3
"""Summarize diagnostics for saved emcee ensembles from Lectures 18-19."""

from __future__ import annotations

import argparse
from pathlib import Path

import emcee
import numpy as np
import pandas as pd


def load_ensemble(path: Path, discard: int):
    """Load one production chain and its metadata from the Lecture 18 NPZ format."""
    with np.load(path, allow_pickle=False) as saved:
        if "chain" not in saved:
            raise ValueError(f"{path} does not contain a 'chain' array")
        chain = np.asarray(saved["chain"], dtype=float)
        names = saved["parameter_names"].astype(str).tolist()
        acceptance = np.asarray(saved["acceptance_fraction"], dtype=float)
        seed = int(saved["seed"]) if "seed" in saved else -1
        data_seed = int(saved["data_seed"]) if "data_seed" in saved else -1
        chain_id = int(saved["chain_id"]) if "chain_id" in saved else -1

    if chain.ndim != 3:
        raise ValueError(
            f"Expected chain axes (steps, walkers, parameters), got {chain.shape} in {path}"
        )
    if chain.shape[2] != len(names):
        raise ValueError(f"Parameter-name count does not match chain shape in {path}")
    if acceptance.shape != (chain.shape[1],):
        raise ValueError(f"Acceptance fractions must have one value per walker in {path}")
    if discard < 0 or discard >= chain.shape[0]:
        raise ValueError(f"Discard must be in [0, {chain.shape[0] - 1}] for {path}")

    return {
        "path": path,
        "chain": chain[discard:],
        "names": names,
        "acceptance": acceptance,
        "seed": seed,
        "data_seed": data_seed,
        "chain_id": chain_id,
    }


def split_rhat(chains: np.ndarray) -> np.ndarray:
    """Compute basic split-Rhat for chains shaped (chains, draws, parameters)."""
    n_chains, n_draws, n_parameters = chains.shape
    if n_chains < 2:
        raise ValueError("Split-Rhat requires at least two independent ensembles")
    half = n_draws // 2
    if half < 2:
        raise ValueError("Each chain needs at least four draws for split-Rhat")

    split = np.concatenate([chains[:, :half, :], chains[:, -half:, :]], axis=0)
    n = split.shape[1]
    within = np.mean(np.var(split, axis=1, ddof=1), axis=0)
    between = n * np.var(np.mean(split, axis=1), axis=0, ddof=1)
    variance_estimate = ((n - 1) / n) * within + between / n
    return np.sqrt(variance_estimate / within)


def diagnose_ensembles(ensembles: list[dict]):
    """Calculate per-ensemble autocorrelation/ESS and cross-ensemble split-Rhat."""
    reference_names = ensembles[0]["names"]
    reference_data_seed = ensembles[0]["data_seed"]
    seen_paths = set()
    seen_seeds = set()
    for ensemble in ensembles:
        if ensemble["names"] != reference_names:
            raise ValueError("All input ensembles must use the same parameter names/order")
        if ensemble["data_seed"] != reference_data_seed:
            raise ValueError("All input ensembles must use the same fixed data seed")
        resolved_path = ensemble["path"].resolve()
        if resolved_path in seen_paths:
            raise ValueError("Each --input must name a different ensemble file")
        seen_paths.add(resolved_path)
        if ensemble["seed"] >= 0:
            if ensemble["seed"] in seen_seeds:
                raise ValueError("Independent ensembles must use distinct sampler seeds")
            seen_seeds.add(ensemble["seed"])

    chain_rows = []
    selected_walkers = []
    common_draws = min(item["chain"].shape[0] for item in ensembles)

    for item in ensembles:
        chain = item["chain"]
        # emcee estimates integrated autocorrelation time across the ensemble walkers.
        tau_int = emcee.autocorr.integrated_time(chain, tol=0)
        flat = chain.reshape(-1, chain.shape[-1])
        ess = chain.shape[0] * chain.shape[1] / tau_int
        posterior_sd = np.std(flat, axis=0, ddof=1)
        mcse = posterior_sd / np.sqrt(ess)
        acceptance_mean = float(np.mean(item["acceptance"]))

        for index, name in enumerate(reference_names):
            chain_rows.append({
                "file": str(item["path"]),
                "chain_id": item["chain_id"],
                "seed": item["seed"],
                "parameter": name,
                "integrated_autocorrelation_time": tau_int[index],
                "effective_sample_size": ess[index],
                "posterior_standard_deviation": posterior_sd[index],
                "mean_MCSE": mcse[index],
                "mean_acceptance_fraction": acceptance_mean,
            })

        # Use one walker per independently run ensemble for between-run R-hat.
        selected_walkers.append(chain[:common_draws, 0, :])

    rhat_rows = []
    if len(ensembles) >= 2:
        rhat = split_rhat(np.stack(selected_walkers))
        rhat_rows = [
            {"parameter": name, "split_Rhat": rhat[index]}
            for index, name in enumerate(reference_names)
        ]
    return pd.DataFrame(chain_rows), pd.DataFrame(rhat_rows)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Calculate emcee autocorrelation, ESS, MCSE, and (with independent runs) split-Rhat."
    )
    parser.add_argument("--input", type=Path, action="append", required=True,
                        help="saved emcee NPZ; repeat once per independently run ensemble")
    parser.add_argument("--discard", type=int, default=0,
                        help="initial stored draws to discard from each input")
    parser.add_argument("--output", type=Path, default=None,
                        help="optional CSV path for per-ensemble diagnostics")
    return parser.parse_args()


def main():
    args = parse_args()
    ensembles = [load_ensemble(path, args.discard) for path in args.input]
    chain_diagnostics, rhat_diagnostics = diagnose_ensembles(ensembles)

    print("Per-ensemble diagnostics:")
    print(chain_diagnostics.to_string(index=False, float_format=lambda value: f"{value:.3f}"))
    if len(rhat_diagnostics):
        print("\nSplit-Rhat from one walker in each independent ensemble:")
        print(rhat_diagnostics.to_string(index=False, float_format=lambda value: f"{value:.3f}"))
    else:
        print("\nSplit-Rhat not calculated: provide at least two independent ensemble files.")
        print("Do not treat walkers within one emcee ensemble as independent chains.")

    if args.output is not None:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        chain_diagnostics.to_csv(args.output, index=False)
        print(f"\nSaved per-ensemble diagnostics to {args.output}")
        if len(rhat_diagnostics):
            rhat_output = args.output.with_name(
                f"{args.output.stem}_rhat{args.output.suffix}"
            )
            rhat_diagnostics.to_csv(rhat_output, index=False)
            print(f"Saved split-Rhat diagnostics to {rhat_output}")


if __name__ == "__main__":
    main()
