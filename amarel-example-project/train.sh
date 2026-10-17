#!/bin/bash
#SBATCH --job-name=pytorch
#SBATCH --partition=gpu
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --gres=gpu:1
#SBATCH --mem=8G
#SBATCH --time=00:15:00
#SBATCH --output=training-%j.out

set -e

# Navigate to the project directory
cd "$SLURM_SUBMIT_DIR"

# Print information about the allocated resources
echo "Job ID: $SLURM_JOB_ID"
echo "Hostname: $(hostname)"
echo "Start time: $(date)"

nvidia-smi

# Run the training script
./.venv/bin/python -u train.py

echo "End time: $(date)"