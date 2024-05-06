"""



#python openstereo/main.py --config ./configs/igev/igev_sceneflow.yaml --scope val

export CUDA_VISIBLE_DEVICES=0
python openstereo/main.py --config ./configs/aanet/AANet_kitti.yaml --scope train --no_distribute --restore_hint ./model/AANet_SceneFlow.pt

python openstereo/main.py --config ./configs/aanet/AANet_custom.yaml --scope test_kitti --no_distribute --restore_hint ./model/AANet_SceneFlow_lamb_b64_288_4e3_epoch_050.pt
python openstereo/main.py --config ./configs/aanet/AANet_custom.yaml --scope test_kitti --no_distribute --restore_hint ./model/official/AANet_SceneFlow.pt
python openstereo/main.py --config ./configs/aanet/AANet_custom.yaml --scope test_kitti --no_distribute --restore_hint ./model/hk_camera/AANet_SceneFlow_lamb_b64_288_4e3_epoch_030.pt

python openstereo/main.py --config ./configs/aanet/AANet_custom.yaml --scope train --no_distribute --restore_hint ./model/official/AANet_SceneFlow.pt

python openstereo/main.py --config ./configs/aanet/AANet_custom.yaml --scope train --no_distribute --restore_hint ./model/official/AANet_SceneFlow.pt

python openstereo/main.py --config ./configs/sttr/STTR_kitti.yaml --scope train --no_distribute --restore_hint ./model/official/AANet_SceneFlow.pt

###### huger
python openstereo/main.py --config ./configs/aanet/AANet_custom.yaml --scope train --no_distribute --restore_hint ./model/official/AANet_SceneFlow.pt
python openstereo/main.py --config ./configs/aanet/AANet_custom.yaml --scope test_kitti --no_distribute --restore_hint ./model/hk_camera/AANet_SceneFlow_lamb_b64_288_4e3_epoch_070.pt

python openstereo/main.py --config ./configs/aanet/AANet_custom.yaml --scope train --no_distribute --restore_hint ./model/hk_camera/AANet_SceneFlow_lamb_b64_288_4e3_epoch_070.pt
python openstereo/main.py --config ./configs/sttr/STTR_custom.yaml --scope train --no_distribute --restore_hint ./model/official/STTR-Stereo_FlyingThings3DSubset_epoch_08.pt
python openstereo/main.py --config ./configs/msnet/MSNet3D_custom.yaml --scope train --no_distribute

python openstereo/main.py --config ./configs/sttr/STTR_custom.yaml --scope test_kitti --no_distribute --restore_hint ./model/hk_camera/STTR-Stereo_custom_epoch_050.pt
python openstereo/main.py --config ./configs/msnet/MSNet2D_custom.yaml --scope test_kitti --no_distribute --restore_hint ./output/custom/MSNet/MSNet2D_SceneFlow/checkpoints/MSNet2D_SceneFlow_epoch_002.pt
python openstereo/main.py --config ./configs/msnet/MSNet2D_custom.yaml --scope train --no_distribute
python openstereo/main.py --config ./configs/msnet/MSNet3D_custom.yaml --scope test_kitti --no_distribute --restore_hint ./output/custom/MSNet/MSNet3D_SceneFlow/checkpoints/MSNet3D_SceneFlow_epoch_001.pt
python openstereo/main.py --config ./configs/msnet/MSNet3D_custom.yaml --scope onnx --no_distribute --restore_hint ./output/custom/MSNet/MSNet3D_SceneFlow/checkpoints/MSNet3D_SceneFlow_epoch_001.pt

"""