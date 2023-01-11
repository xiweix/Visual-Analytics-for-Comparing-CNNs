# pip install importlib_resources
import os
import numpy as np
import torch
import torch.nn.functional as F
import torchvision.models as models
from torchvision.utils import save_image
from scorecam_utils import load_image, apply_transforms, visualize_cam
from scorecam.scorecam import ScoreCAM

def scorecamMain(model_list, img_name_list, dataset_path, output_path):
    cam_dict = dict()
    if 'mobilenet_v2' in model_list:
        mobilenet_v2 = models.mobilenet_v2(pretrained=True).eval()
        if torch.cuda.is_available():
            mobilenet_v2.cuda()
        mobilenet_v2_model_dict = dict(type='mobilenet_v2', arch=mobilenet_v2, layer_name='features_18',input_size=(224, 224))
        mobilenet_v2_scorecam = ScoreCAM(mobilenet_v2_model_dict)
        cam_dict['mobilenet_v2'] = mobilenet_v2_scorecam
    if 'alexnet' in model_list:
        alexnet = models.alexnet(pretrained=True).eval()
        if torch.cuda.is_available():
            alexnet.cuda()
        alexnet_model_dict = dict(type='alexnet', arch=alexnet, layer_name='features_11',input_size=(224, 224))
        alexnet_scorecam = ScoreCAM(alexnet_model_dict)
        cam_dict['alexnet'] = alexnet_scorecam
        # predicted_class = alexnet(input_).max(1)[-1]
    if 'resnet18' in model_list:
        resnet18 = models.resnet18(pretrained=True).eval()
        if torch.cuda.is_available():
            resnet18.cuda()
        resnet18_model_dict = dict(type='resnet18', arch=resnet18, layer_name='layer4',input_size=(224, 224))
        resnet18_scorecam = ScoreCAM(resnet18_model_dict)
        cam_dict['resnet18'] = resnet18_scorecam
    if 'resnet34' in model_list:
        resnet34 = models.resnet34(pretrained=True).eval()
        if torch.cuda.is_available():
            resnet34.cuda()
        resnet34_model_dict = dict(type='resnet34', arch=resnet34, layer_name='layer4',input_size=(224, 224))
        resnet34_scorecam = ScoreCAM(resnet34_model_dict)
        cam_dict['resnet34'] = resnet34_scorecam
    if 'resnet50' in model_list:
        resnet50 = models.resnet50(pretrained=True).eval()
        if torch.cuda.is_available():
            resnet50.cuda()
        resnet50_model_dict = dict(type='resnet50', arch=resnet50, layer_name='layer4',input_size=(224, 224))
        resnet50_scorecam = ScoreCAM(resnet50_model_dict)
        cam_dict['resnet50'] = resnet50_scorecam
    if 'resnet101' in model_list:
        resnet101 = models.resnet101(pretrained=True).eval()
        if torch.cuda.is_available():
            resnet101.cuda()
        resnet101_model_dict = dict(type='resnet101', arch=resnet101, layer_name='layer4',input_size=(224, 224))
        resnet101_scorecam = ScoreCAM(resnet101_model_dict)
        cam_dict['resnet101'] = resnet101_scorecam
    if 'resnet152' in model_list:
        resnet152 = models.resnet152(pretrained=True).eval()
        if torch.cuda.is_available():
            resnet152.cuda()
        resnet152_model_dict = dict(type='resnet152', arch=resnet152, layer_name='layer4',input_size=(224, 224))
        resnet152_scorecam = ScoreCAM(resnet152_model_dict)
        cam_dict['resnet152'] = resnet152_scorecam
    if 'densenet121' in model_list:
        densenet121 = models.densenet121(pretrained=True).eval()
        if torch.cuda.is_available():
            densenet121.cuda()
        densenet121_model_dict = dict(type='densenet121', arch=densenet121, layer_name='features_norm5',input_size=(224, 224))
        densenet121_scorecam = ScoreCAM(densenet121_model_dict)
        cam_dict['densenet121'] = densenet121_scorecam
    if 'densenet161' in model_list:
        densenet161 = models.densenet161(pretrained=True).eval()
        if torch.cuda.is_available():
            densenet161.cuda()
        densenet161_model_dict = dict(type='densenet161', arch=densenet161, layer_name='features_norm5',input_size=(224, 224))
        densenet161_scorecam = ScoreCAM(densenet161_model_dict)
        cam_dict['densenet161'] = densenet161_scorecam
    if 'densenet169' in model_list:
        densenet169 = models.densenet169(pretrained=True).eval()
        if torch.cuda.is_available():
            densenet169.cuda()
        densenet169_model_dict = dict(type='densenet169', arch=densenet169, layer_name='features_norm5',input_size=(224, 224))
        densenet169_scorecam = ScoreCAM(densenet169_model_dict)
        cam_dict['densenet169'] = densenet169_scorecam
    if 'densenet201' in model_list:
        densenet201 = models.densenet201(pretrained=True).eval()
        if torch.cuda.is_available():
            densenet201.cuda()
        densenet201_model_dict = dict(type='densenet201', arch=densenet201, layer_name='features_norm5',input_size=(224, 224))
        densenet201_scorecam = ScoreCAM(densenet201_model_dict)
        cam_dict['densenet201'] = densenet201_scorecam
    if 'squeezenet1_1' in model_list:
        squeezenet1_1 = models.squeezenet1_1(pretrained=True).eval()
        if torch.cuda.is_available():
            squeezenet1_1.cuda()
        squeezenet1_1_model_dict = dict(type='squeezenet1_1', arch=squeezenet1_1, layer_name='features_12',input_size=(224, 224))
        squeezenet1_1_scorecam = ScoreCAM(squeezenet1_1_model_dict)
        cam_dict['squeezenet1_1'] = squeezenet1_1_scorecam
    if 'shufflenet_v2_x0_5' in model_list:
        shufflenet_v2_x0_5 = models.shufflenet_v2_x0_5(pretrained=True).eval()
        if torch.cuda.is_available():
            shufflenet_v2_x0_5.cuda()
        shufflenet_v2_x0_5_model_dict = dict(type='shufflenet_v2_x0_5', arch=shufflenet_v2_x0_5, layer_name='conv5',input_size=(224, 224))
        shufflenet_v2_x0_5_scorecam = ScoreCAM(shufflenet_v2_x0_5_model_dict)
        cam_dict['shufflenet_v2_x0_5'] = shufflenet_v2_x0_5_scorecam
    j = 0
    for img_name in img_name_list:
        # Load image
        print(f'score-cam {img_name} {j}/{len(img_name_list)}')
        img_dir = os.path.join(dataset_path, 'ILSVRC2012_img_val')
        img_path = os.path.join(img_dir, img_name)
        input_image = load_image(img_path)
        input_ = apply_transforms(input_image)
        if torch.cuda.is_available():
            input_ = input_.cuda()
        # define the output direction
        base_name = os.path.splitext(img_name)[0]
        output_dir = os.path.join(output_path, base_name)
        os.makedirs(output_dir, exist_ok=True)
        i = 0
        for scorecam in cam_dict.values():
            model_name = list(cam_dict)[i]
            print(model_name)
            if not os.path.exists(os.path.join(output_dir, f'{model_name}_scorecam.png')):
                scorecam_map = scorecam(input_)
                scorecam_map = np.uint8(255 * scorecam_map.squeeze().cpu())
                np.save(os.path.join(output_dir, f'{model_name}_scorecam_mask.npy'), scorecam_map)

                score_heat, score_img = visualize_cam(scorecam_map, input_.cpu())
                save_image(score_heat, os.path.join(output_dir, f'{model_name}_scorecam.png'))
                save_image(score_img, os.path.join(output_dir, f'{model_name}_scorecam_img.png'))
            i += 1
            # basic_visualize(input_.cpu(), scorecam_map.type(torch.FloatTensor).cpu(),model_name=model_name,output_dir=output_dir)
        j += 1
        
