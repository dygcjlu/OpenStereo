CUDA_VISIBLE_DEVICES=3,4 python -m torch.distributed.launch --nproc_per_node=2 -- openstereo/main.py --cfgs ./configs/sttr/STTR_SceneFlow.yaml --phase train 2>&1 |tee logs/sttr_stereo.txt