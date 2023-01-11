import os
import numpy as np
import skimage.transform
import torch
import torch.nn as nn
import torch.nn. functional as F

from PIL import Image
import matplotlib.pyplot as plt
from torchvision import models, transforms
from torchvision.utils import save_image

from smoothgradcam import CAM, GradCAM, GradCAMpp, SmoothGradCAMpp
from smooth_utils.visualize import visualize2, reverse_normalize, smoothcam_to_img
from smooth_utils.imagenet_labels import label2idx, idx2label

def smooth_main(dataset_path, image_name, model_name, output_path):
    useCUDA = torch.cuda.is_available()
    torch.cuda.empty_cache()
    # if not os.path.exists(os.path.join(output_dir, f'{model_name}_smoothgradcampp_cam.npy')):
    # cam_dict = dict()

    model = getattr(models, model_name)(pretrained=True)
    model.eval()
    if useCUDA:
        model.cuda()

    # process image
    img_path = os.path.join(dataset_path, 'ILSVRC2012_img_val', image_name)
    image = Image.open(img_path).convert('RGB')
    base_name = os.path.splitext(image_name)[0]
    output_dir = os.path.join(output_path, base_name)
    os.makedirs(output_dir, exist_ok=True)
    normalize = transforms.Normalize(
      mean=[0.485, 0.456, 0.406],
      std=[0.229, 0.224, 0.225]
    )
    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        normalize
    ])

    # for idx in range(3):
    target_layer = model.maxpool
    # print(target_layer)
    wrapped_model = SmoothGradCAMpp(model, target_layer, n_samples=25, stdev_spread=0.15)
    layer_name = 'res152_ly0'
    print(layer_name)

    # convert image to tensor
    tensor = preprocess(image)

    # reshape 4D tensor (N, C, H, W)
    tensor = tensor.unsqueeze(0)
    if useCUDA:
        tensor = tensor.cuda()

    cam, idx = wrapped_model(tensor)
    cam = cam.cpu()
    # print(idx2label[idx])
    img = reverse_normalize(tensor)
    # plt.imshow(cam.squeeze().numpy(), alpha=0.5, cmap='jet')
    # save_image(cam, os.path.join(output_dir, f'{model_name}_smoothgradcampp_sq.JPEG'))
    visualize2(img, cam, output_dir, layer_name)

    # else:
    #     smoothcam_to_img(dataset_path, image_name, model_name, output_dir)