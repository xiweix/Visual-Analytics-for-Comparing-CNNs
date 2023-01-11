import os
import torch
import torch.nn.functional as F

import numpy as np
import cv2
from PIL import Image
from torchvision import transforms
from torchvision.utils import save_image

def reverse_normalize(x, mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]):
    x[:, 0, :, :] = x[:, 0, :, :] * std[0] + mean[0]
    x[:, 1, :, :] = x[:, 1, :, :] * std[1] + mean[1]
    x[:, 2, :, :] = x[:, 2, :, :] * std[2] + mean[2]
    return x


def visualize2(img, cam, out_path, layer_name):
    """
    Synthesize an image with CAM to make a result image.
    Args:
        img: (Tensor) shape => (1, 3, H, W)
        cam: (Tensor) shape => (1, 1, H', W')
    Return:
        synthesized image (Tensor): shape =>(1, 3, H, W)
    """

    _, _, H, W = img.shape

    # np.save(os.path.join(out_path, f'{layer_name}_smoothgradcampp_cam0_ly3.npy'), cam)

    cam = F.interpolate(cam, size=(H, W), mode='bilinear', align_corners=False)
    cam = np.uint8(255 * cam.squeeze())
    # print('test, cam: ', type(cam), cam.shape)
    # np.save(os.path.join(out_path, f'{layer_name}_smoothgradcampp_cam.npy'), cam)
    np.save(os.path.join(out_path, f'{layer_name}_smoothgradcampp_cam.npy'), cam)

    heatmap = cv2.applyColorMap(cam, cv2.COLORMAP_VIRIDIS)

    heatmap = torch.from_numpy(heatmap.transpose(2, 0, 1))
    heatmap = heatmap.float() / 255
    b, g, r = heatmap.split(1)
    heatmap = torch.cat([r, g, b])

    result = heatmap + img.cpu()
    result = result.div(result.max())

    # save_image(heatmap, os.path.join(out_path, f'{layer_name}_smoothgradcampp.png'))
    # save_image(result, os.path.join(out_path, f'{layer_name}_smoothgradcampp_img.png'))
    save_image(heatmap, os.path.join(out_path, f'{layer_name}_smoothgradcampp.png'))
    save_image(result, os.path.join(out_path, f'{layer_name}_smoothgradcampp_img.png'))

def visualize(img, cam, out_path, model_name):
    """
    Synthesize an image with CAM to make a result image.
    Args:
        img: (Tensor) shape => (1, 3, H, W)
        cam: (Tensor) shape => (1, 1, H', W')
    Return:
        synthesized image (Tensor): shape =>(1, 3, H, W)
    """

    _, _, H, W = img.shape

    # np.save(os.path.join(out_path, f'{model_name}_smoothgradcampp_cam0_ly3.npy'), cam)

    cam = F.interpolate(cam, size=(H, W), mode='bilinear', align_corners=False)
    cam = np.uint8(255 * cam.squeeze())
    # print('test, cam: ', type(cam), cam.shape)
    # np.save(os.path.join(out_path, f'{model_name}_smoothgradcampp_cam.npy'), cam)
    np.save(os.path.join(out_path, f'{model_name}_smoothgradcampp_cam.npy'), cam)

    heatmap = cv2.applyColorMap(cam, cv2.COLORMAP_VIRIDIS)

    heatmap = torch.from_numpy(heatmap.transpose(2, 0, 1))
    heatmap = heatmap.float() / 255
    b, g, r = heatmap.split(1)
    heatmap = torch.cat([r, g, b])

    result = heatmap + img.cpu()
    result = result.div(result.max())

    # save_image(heatmap, os.path.join(out_path, f'{model_name}_smoothgradcampp.png'))
    # save_image(result, os.path.join(out_path, f'{model_name}_smoothgradcampp_img.png'))
    save_image(heatmap, os.path.join(out_path, f'{model_name}_smoothgradcampp.png'))
    save_image(result, os.path.join(out_path, f'{model_name}_smoothgradcampp_img.png'))

def smoothcam_to_img(dataset_path, image_name, model_name, output_path):
    img_path = os.path.join(dataset_path, 'ILSVRC2012_img_val', image_name)
    image = Image.open(img_path).convert('RGB')
    base_name = os.path.splitext(image_name)[0]
    output_dir = os.path.join(output_path, base_name)
    # preprocessing. mean and std from ImageNet
    normalize = transforms.Normalize(
      mean=[0.485, 0.456, 0.406],
      std=[0.229, 0.224, 0.225]
    )

    preprocess = transforms.Compose([
        transforms.Resize((224, 224)),
        transforms.ToTensor(),
        normalize
    ])

    # convert image to tensor
    tensor = preprocess(image)

    # reshape 4D tensor (N, C, H, W)
    tensor = tensor.unsqueeze(0)

    img = reverse_normalize(tensor)
    cam = np.load(os.path.join(output_dir, f'{model_name}_smoothgradcampp_cam.npy'))

    heatmap = cv2.applyColorMap(cam, cv2.COLORMAP_VIRIDIS)

    heatmap = torch.from_numpy(heatmap.transpose(2, 0, 1))
    heatmap = heatmap.float() / 255
    b, g, r = heatmap.split(1)
    heatmap = torch.cat([r, g, b])

    result = heatmap + img.cpu()
    result = result.div(result.max())

    save_image(heatmap, os.path.join(output_dir, f'{model_name}_smoothgradcampp.png'))
    save_image(result, os.path.join(output_dir, f'{model_name}_smoothgradcampp_img.png'))