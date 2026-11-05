#!/usr/bin/env python3
"""Evaluate the Lecture 17 Ramsey posterior on a two-parameter grid.

The script is intentionally command-line driven so students can compare grid
resolution and priors locally, then submit independent parameter slices or
larger grids as HPC jobs.
"""

from __future__ import annotations

import argparse
from pathlib import Path

import numpy as np
from scipy.special import logsumexp
from scipy.stats import binom


TRUE = (2.40, 0.78)
OMEGA = 2.0 * np.pi * 0.85
PHASE = 0.25
TAU_PRIOR_MIN = 0.4
TAU_PRIOR_MAX = 6.0
CONTRAST_PRIOR_MIN = 0.0
CONTRAST_PRIOR_MAX = 1.0


def ramsey_probability(t, contrast, tau):
    probability = 0.5 * (1.0 + contrast * np.exp(-t / tau) * np.cos(OMEGA * t + PHASE))
    return np.clip(probability, 1.0e-12, 1.0 - 1.0e-12)


def log_posterior(tau, contrast, times, shots, counts, prior):
    if (tau <= 0.0 or not CONTRAST_PRIOR_MIN <= contrast <= CONTRAST_PRIOR_MAX):
        return -np.inf
    probability = ramsey_probability(times, contrast, tau)
    log_likelihood = np.sum(binom.logpmf(counts, shots, probability))
    if prior == "broad":
        return log_likelihood if TAU_PRIOR_MIN <= tau <= TAU_PRIOR_MAX else -np.inf
    if prior == "calibration":
        return log_likelihood - 0.5 * ((tau - 2.5) / 0.35) ** 2
    raise ValueError(f"unknown prior: {prior}")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--tau-points", type=int, default=150)
    parser.add_argument("--contrast-points", type=int, default=140)
    parser.add_argument("--prior", choices=["broad", "calibration"], default="broad")
    parser.add_argument("--seed", type=int, default=1701)
    parser.add_argument("--output", type=Path, default=Path("posterior_grid.npz"))
    args = parser.parse_args()

    rng = np.random.default_rng(args.seed)
    times = np.linspace(0.0, 5.0, 31)
    shots = np.full(times.size, 250, dtype=int)
    counts = rng.binomial(shots, ramsey_probability(times, TRUE[1], TRUE[0]))
    tau_grid = np.linspace(TAU_PRIOR_MIN, TAU_PRIOR_MAX, args.tau_points)
    contrast_grid = np.linspace(CONTRAST_PRIOR_MIN, CONTRAST_PRIOR_MAX, args.contrast_points)
    log_grid = np.empty((contrast_grid.size, tau_grid.size))
    for i, contrast in enumerate(contrast_grid):
        for j, tau in enumerate(tau_grid):
            log_grid[i, j] = log_posterior(tau, contrast, times, shots, counts, args.prior)
    posterior = np.exp(log_grid - logsumexp(log_grid))
    args.output.parent.mkdir(parents=True, exist_ok=True)
    np.savez(args.output, tau_grid=tau_grid, contrast_grid=contrast_grid,
             log_posterior=log_grid, posterior=posterior, counts=counts, times=times)
    print(f"saved {args.output} with shape {posterior.shape}; normalization={posterior.sum():.8f}")


if __name__ == "__main__":
    main()
