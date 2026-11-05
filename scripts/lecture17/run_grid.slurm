#!/bin/bash
#SBATCH --job-name=ramsey_grid
#SBATCH --output=slurm_logs/ramsey_grid_%j.out
#SBATCH --error=slurm_logs/ramsey_grid_%j.err
#SBATCH --time=00:30:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G

set -euo pipefail

if [[ $# -ne 3 ]]; then
  echo "Usage: sbatch scripts/lecture17/run_grid.slurm TAU_POINTS CONTRAST_POINTS LABEL"
  echo "Example: sbatch scripts/lecture17/run_grid.slurm 300 280 posterior_300x280"
  exit 2
fi

TAU_POINTS=$1
CONTRAST_POINTS=$2
LABEL=$3

cd "${SLURM_SUBMIT_DIR}"
source /usr/local/etc/sciclone.bashrc
source .venv/bin/activate
mkdir -p outputs

python -u scripts/lecture17/grid_posterior.py \
  --tau-points "${TAU_POINTS}" \
  --contrast-points "${CONTRAST_POINTS}" \
  --prior broad \
  --seed 69017 \
  --output "outputs/${LABEL}.npz"
