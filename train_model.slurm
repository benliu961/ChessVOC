#!/bin/bash
#SBATCH --job-name=train_model   # create a short name for your job
#SBATCH --output=slurm-%A.%a.out # stdout file
#SBATCH --error=slurm-%A.%a.err  # stderr file
#SBATCH --nodes=1                # node count
#SBATCH --ntasks=1               # total number of tasks across all nodes
#SBATCH --gres=gpu:1             # number of gpus per node
#SBATCH --cpus-per-task=12       # cpu-cores per task (>1 if multi-threaded tasks)
#SBATCH --mem=8G                 # total memory per node (4 GB per cpu-core is default)
#SBATCH --time=24:00:00          # total run time limit (HH:MM:SS)
#SBATCH --mail-type=all          # send email on job start, end and fault
#SBATCH --mail-user=bxliu@princeton.edu

module purge
module load anaconda3/2022.10
conda activate chess-env

python train.py --batch-size 16384 --threads 2 --num-workers 2 --gpus 1 --no-smart-fen-skipping --no-wld-fen-skipping train_data.binpack val_data.binpack