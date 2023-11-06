#!/bin/bash
#SBATCH --partition=SCSEGPU_UG
#SBATCH --qos=normal
#SBATCH --gres=gpu:1
#SBATCH --nodes=1
#SBATCH --mem=64G
#SBATCH --job-name=train_resnet
#SBATCH --output=output/output_%j_%x.out 
#SBATCH --error=error/error_%j_%x.err 


module load anaconda
source activate nndl_gpu

cd /home/UG/keek0005/NNDL/Deformable-Convolution

python -W ignore main.py \
                --dataset "fashionmnist" \
                --resnet_version "152" \
                --with_deformable_conv 0 0 0 0\
                --unfreeze_conv 0 0 9 3\
                --unfreeze_offset \
                --unfreeze_fc \
                --early_stopping \
                --patience 10 \
                --mode "min" \
                --min_delta 0 \
                --restore_best_weight \
                --learning_rate 0.0001 \
                --train_batch_size 128 \
                --eval_batch_size 128 \
                --num_epochs 200 \
