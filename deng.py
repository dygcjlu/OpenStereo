"""



#python openstereo/main.py --config ./configs/igev/igev_sceneflow.yaml --scope val

export CUDA_VISIBLE_DEVICES=0
python openstereo/main.py --config ./configs/aanet/AANet_kitti.yaml --scope train --no_distribute --restore_hint ./model/AANet_SceneFlow.pt

python openstereo/main.py --config ./configs/aanet/AANet_kitti.yaml --scope test_kitti --no_distribute --restore_hint ./model/AANet_SceneFlow_lamb_b64_288_4e3_epoch_055.pt

"""