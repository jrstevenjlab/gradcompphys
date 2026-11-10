#!/usr/bin/env python3
"""Run a reproducible Ramsey posterior ensemble with emcee (Lecture 18)."""

from __future__ import annotations

import argparse
from multiprocessing import Pool
from pathlib import Path

import emcee
import numpy as np
from scipy.stats import binom


# The simulated signal uses these known values to generate the fixed data set.
TRUE_PARAMETERS = {
    "tau": 2.40,
    "contrast": 0.78,
    "omega": 2.0 * np.pi * 0.85,
    "phase": 0.25,
}
DATA_SEED = 69017
TAU_PRIOR = (0.4, 6.0)
CONTRAST_PRIOR = (0.0, 1.0)
OMEGA_PRIOR = (2.0 * np.pi * 0.70, 2.0 * np.pi * 1.00)
PHASE_PRIOR = (-np.pi, np.pi)


def ramsey_probability(times, tau, contrast, omega, phase):
    """Evaluate the Ramsey excited-state probability at each delay."""
    probability = 0.5 * (
        1.0 + contrast * np.exp(-times / tau) * np.cos(omega * times + phase)
    )
    return np.clip(probability, 1.0e-12, 1.0 - 1.0e-12)


class RamseyLogPosterior:
    """Picklable log-posterior callable, usable by emcee worker processes."""

    def __init__(self, times, shots, counts, dimensions):
        self.times = times
        self.shots = shots
        self.counts = counts
        self.dimensions = dimensions

    def __call__(self, parameters):
        if self.dimensions == 2:
            tau, contrast = parameters
            omega = TRUE_PARAMETERS["omega"]
            phase = TRUE_PARAMETERS["phase"]
            if not (TAU_PRIOR[0] <= tau <= TAU_PRIOR[1]
                    and CONTRAST_PRIOR[0] <= contrast <= CONTRAST_PRIOR[1]):
                return -np.inf
        else:
            tau, contrast, omega, phase = parameters
            if not (
                TAU_PRIOR[0] <= tau <= TAU_PRIOR[1]
                and CONTRAST_PRIOR[0] <= contrast <= CONTRAST_PRIOR[1]
                and OMEGA_PRIOR[0] <= omega <= OMEGA_PRIOR[1]
                and PHASE_PRIOR[0] <= phase <= PHASE_PRIOR[1]
            ):
                return -np.inf

        # The binomial log likelihood is the log posterior up to the uniform-prior constant.
        probability = ramsey_probability(self.times, tau, contrast, omega, phase)
        return float(np.sum(binom.logpmf(self.counts, self.shots, probability)))


def make_data(data_seed: int):
    """Recreate the same seeded finite-shot Ramsey data used in the notebook."""
    rng = np.random.default_rng(data_seed)
    times = np.linspace(0.0, 5.0, 31)
    shots = np.full(times.size, 250, dtype=int)
    probability = ramsey_probability(times, **TRUE_PARAMETERS)
    counts = rng.binomial(shots, probability)
    return times, shots, counts


def parse_args():
    parser = argparse.ArgumentParser(
        description="Sample the Lecture 18 Ramsey posterior using emcee."
    )
    parser.add_argument("--dimensions", type=int, choices=(2, 4), default=2,
                        help="infer (tau, contrast), or also (omega, phase)")
    parser.add_argument("--steps", type=int, default=5000,
                        help="number of retained production steps")
    parser.add_argument("--warmup", type=int, default=1000,
                        help="number of initial burn-in steps to discard")
    parser.add_argument("--walkers", type=int, default=None,
                        help="ensemble size (defaults to 32 in 2D, 48 in 4D)")
    parser.add_argument("--workers", type=int, default=1,
                        help="likelihood worker processes; use 1 to disable multiprocessing")
    parser.add_argument("--seed", type=int, default=1801,
                        help="base sampler seed; chain ID is added for independent runs")
    parser.add_argument("--data-seed", type=int, default=DATA_SEED,
                        help="seed for regenerating the fixed synthetic data")
    parser.add_argument("--chain-id", type=int, default=0,
                        help="independent run ID, also used to vary the sampler seed")
    parser.add_argument("--output", type=Path, default=None,
                        help="output .npz path (defaults to outputs/ramsey_emcee_...)")
    return parser.parse_args()


def main():
    args = parse_args()
    if args.steps < 1 or args.warmup < 0:
        raise SystemExit("--steps must be positive and --warmup cannot be negative")
    if args.workers < 1 or args.chain_id < 0:
        raise SystemExit("--workers must be positive and --chain-id cannot be negative")

    dimensions = args.dimensions
    parameter_names = (
        ["tau", "contrast"] if dimensions == 2
        else ["tau", "contrast", "omega", "phase"]
    )
    nwalkers = args.walkers or (32 if dimensions == 2 else 48)
    if nwalkers < 2 * dimensions:
        raise SystemExit(f"emcee needs at least {2 * dimensions} walkers for {dimensions} parameters")

    # Give each independent run a reproducible but distinct random stream.
    sampler_seed = args.seed + args.chain_id
    position_rng = np.random.default_rng(sampler_seed + 1)
    np.random.seed(sampler_seed)

    # Start the walkers in a compact, valid cloud near a plausible parameter point.
    center = np.array([
        TRUE_PARAMETERS[name] for name in parameter_names
    ], dtype=float)
    scales = np.array([0.15, 0.04] if dimensions == 2 else [0.15, 0.04, 0.08, 0.15])
    initial_positions = center + position_rng.normal(size=(nwalkers, dimensions)) * scales

    times, shots, counts = make_data(args.data_seed)
    log_posterior = RamseyLogPosterior(times, shots, counts, dimensions)
    if not np.all(np.isfinite([log_posterior(position) for position in initial_positions])):
        raise SystemExit("An initial walker is outside the prior bounds; adjust the start or scales")

    # Use multiprocessing only when requested; each task evaluates one walker's likelihood.
    output = args.output or Path(
        f"outputs/ramsey_emcee_{dimensions}d_chain{args.chain_id}.npz"
    )
    output.parent.mkdir(parents=True, exist_ok=True)

    def run_sampler(pool=None):
        sampler = emcee.EnsembleSampler(
            nwalkers, dimensions, log_posterior, pool=pool
        )
        if args.warmup:
            state = sampler.run_mcmc(initial_positions, args.warmup, progress=True)
        else:
            state = initial_positions
        sampler.reset()  # Keep only production samples in the saved chain.
        sampler.run_mcmc(state, args.steps, progress=True)
        return sampler

    if args.workers == 1:
        sampler = run_sampler()
    else:
        with Pool(processes=args.workers) as pool:
            sampler = run_sampler(pool)

    # Store the chain in (step, walker, parameter) order plus run metadata.
    np.savez_compressed(
        output,
        chain=sampler.get_chain(),
        log_probability=sampler.get_log_prob(),
        parameter_names=np.asarray(parameter_names),
        warmup_steps=args.warmup,
        production_steps=args.steps,
        walkers=nwalkers,
        dimensions=dimensions,
        seed=sampler_seed,
        data_seed=args.data_seed,
        chain_id=args.chain_id,
        acceptance_fraction=sampler.acceptance_fraction,
    )
    print(f"Saved samples: {output}")
    print(f"Parameters: {', '.join(parameter_names)}")
    print(f"Chain shape (steps, walkers, parameters): {sampler.get_chain().shape}")
    print(f"Mean acceptance fraction: {sampler.acceptance_fraction.mean():.3f}")
    print(f"Sampler seed: {sampler_seed}; data seed: {args.data_seed}")


if __name__ == "__main__":
    main()
