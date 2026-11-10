#!/bin/bash
#SBATCH --job-name=ramsey_emcee
#SBATCH --output=slurm_logs/lecture18_emcee_%A_%a.out
#SBATCH --error=slurm_logs/lecture18_emcee_%A_%a.err
#SBATCH --time=02:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=4G

set -euo pipefail

cd "${SLURM_SUBMIT_DIR}"
source /usr/local/etc/sciclone.bashrc
source .venv/bin/activate

# An array task ID gives each independent ensemble a distinct seed and output file.
CHAIN_ID="${SLURM_ARRAY_TASK_ID:-${CHAIN_ID:-0}}"
DIMENSIONS="${DIMENSIONS:-4}"
WALKERS="${WALKERS:-48}"
WORKERS="${WORKERS:-4}"
STEPS="${STEPS:-20000}"
WARMUP="${WARMUP:-2000}"
SEED="${SEED:-1823}"
DATA_SEED="${DATA_SEED:-69017}"
OUTPUT="${OUTPUT:-outputs/ramsey_emcee_${DIMENSIONS}d_chain${CHAIN_ID}.npz}"

python -u scripts/lecture18/run_mcmc.py \
  --dimensions "${DIMENSIONS}" \
  --walkers "${WALKERS}" \
  --workers "${WORKERS}" \
  --steps "${STEPS}" \
  --warmup "${WARMUP}" \
  --seed "${SEED}" \
  --data-seed "${DATA_SEED}" \
  --chain-id "${CHAIN_ID}" \
  --output "${OUTPUT}"
