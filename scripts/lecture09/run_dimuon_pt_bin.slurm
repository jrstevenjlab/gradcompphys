#!/bin/bash
#SBATCH --job-name=dimuon_pt
#SBATCH --output=slurm_logs/dimuon_pt_%j.out
#SBATCH --error=slurm_logs/dimuon_pt_%j.err
#SBATCH --time=00:20:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=2G

set -euo pipefail

if [[ $# -ne 3 ]]; then
  echo "Usage: sbatch scripts/lecture09/run_dimuon_pt_bin.slurm PT_MIN PT_MAX LABEL"
  echo "Example: sbatch scripts/lecture09/run_dimuon_pt_bin.slurm 0 4 pt_0_4"
  exit 2
fi

PT_MIN=$1
PT_MAX=$2
LABEL=$3

cd "${SLURM_SUBMIT_DIR}"

source .venv/bin/activate
mkdir -p slurm_outputs

python -u scripts/lecture09/dimuon_pt_bootstrap.py \
  --data data/cms_dimuon_jpsi_3000.csv \
  --pt-min "${PT_MIN}" \
  --pt-max "${PT_MAX}" \
  --label "${LABEL}" \
  --n-bootstrap 200 \
  --output-dir slurm_outputs \
  --seed "${SLURM_JOB_ID}"
