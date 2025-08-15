#!/bin/bash
#SBATCH --job-name=source_detection_pipeline
#SBATCH --partition=GPU
#SBATCH --gres=gpu:1
#SBATCH --mem=16GB
#SBATCH --output=testjob-%j-stdout.log
#SBATCH --error=testjob-%j-stderr.log
#SBATCH --time=01:00:00

# Load required modules (adjust based on your cluster setup)
module load python/3.10
module load cuda/11.8           # Adjust CUDA version to match your GPU

# Activate virtual environment (if used)
source ~/venv/bin/activate
./install_deps.sh

# Change to script directory
cd ~/Auto_source_detect_framework/scripts

# Run the pipeline
echo "Submitting Slurm Job"
echo "Starting Detection Framework on GPU node"
./run_pipeline.sh

echo "Pipeline completed on $(hostname) at $(date)"
