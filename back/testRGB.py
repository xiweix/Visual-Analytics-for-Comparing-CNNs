import os
import numpy as np
# from skimage import io
import matplotlib.pyplot as plt
from PIL import Image

dataset_path = os.path.join(os.path.dirname(
    os.path.dirname(os.getcwd())), 'dataset')
root_path = os.path.join(os.path.dirname(
    os.path.dirname(os.getcwd())), 'testRGB')
output_path = os.path.join(os.path.dirname(os.path.dirname(os.getcwd())), 'exp_out')

# img_name_list = [
#   'ILSVRC2012_val_00022313.JPEG',
#   'ILSVRC2012_val_00037486.JPEG',
#   'ILSVRC2012_val_00032469.JPEG',
#   'ILSVRC2012_val_00032626.JPEG',
#   'ILSVRC2012_val_00001716.JPEG',
#   'ILSVRC2012_val_00011111.JPEG'
# ]
# img_name_list = [
#   'ILSVRC2012_val_00029323.JPEG',
#   'ILSVRC2012_val_00025667.JPEG'
# ]
# img_name_list = [
#   'ILSVRC2012_val_00009739.JPEG',
#   'ILSVRC2012_val_00002002.JPEG',
#   'ILSVRC2012_val_00028854.JPEG'
# ]
# img_name_list = [
#   'ILSVRC2012_val_00042339.JPEG',
#   'ILSVRC2012_val_00042344.JPEG',
#   'ILSVRC2012_val_00029133.JPEG',
#   'ILSVRC2012_val_00049285.JPEG',
#   'ILSVRC2012_val_00034410.JPEG',
#   'ILSVRC2012_val_00006824.JPEG',
#   'ILSVRC2012_val_00003139.JPEG',
#   'ILSVRC2012_val_00000531.JPEG',
#   'ILSVRC2012_val_00017278.JPEG',
#   'ILSVRC2012_val_00034747.JPEG',
#   'ILSVRC2012_val_00037538.JPEG'
# ]
img_name_list = ['ILSVRC2012_val_00028622.JPEG']
model_name = 'resnet152'

# filter image based on smooth grad cam++ mask
for img_name in img_name_list:
    base_name = os.path.splitext(img_name)[0]
    output_dir = os.path.join(output_path, base_name)
    write_path = os.path.join(root_path, base_name)
    os.makedirs(write_path, exist_ok=True)

    img_path = os.path.join(dataset_path, 'ILSVRC2012_img_val', img_name)
    image = Image.open(img_path).convert('RGB').resize((224, 224))
    img = np.array(image)

    smooth_res = np.load(os.path.join(output_dir, f'{model_name}_smoothgradcampp_cam.npy'))/255.
    # print(type(smooth_res), smooth_res.shape)
    # print(np.max(smooth_res), np.min(smooth_res))
    idx_list = []
    for i in range(smooth_res.shape[0]):
        for j in range(smooth_res.shape[1]):
            mask_value = smooth_res[i, j]
            if mask_value < 0.5:
                # print('before, R: ', type(img[i, j, 0]), img[i, j, 0])
                # print('before, G: ', type(img[i, j, 1]), img[i, j, 1])
                # print('before, B: ', type(img[i, j, 1]), img[i, j, 1])
                img[i, j, 0] = 0
                img[i, j, 1] = 0
                img[i, j, 2] = 0
                cur_idx = [i, j]
                idx_list.append(cur_idx)
                # print('after: ', type(img[i, j, 0]), img[i, j, 0])
                # print('after: ', type(img[i, j, 1]), img[i, j, 1])
                # print('after: ', type(img[i, j, 2]), img[i, j, 2])
    # print(type(img), img.shape)
    im = Image.fromarray(img)
    im.save(os.path.join(write_path, 'masked.png'))
    np.save(os.path.join(write_path, 'filterout.npy'), idx_list)
    print(len(idx_list), img_name)

for img_name in img_name_list:
    base_name = os.path.splitext(img_name)[0]
    write_path = os.path.join(root_path, base_name)
    maskImgPath = os.path.join(write_path, 'masked.png')
    idx_list = np.load(os.path.join(write_path, 'filterout.npy')).tolist()
    maskImg = Image.open(maskImgPath)
    maskImg = np.array(maskImg)
    # print(maskImg.shape)
    R_channel = []
    G_channel = []
    B_channel = []
    k = 0
    for i in range(224):
        for j in range(224):
            if [i, j] in idx_list:
                k += 1
            else:
                R_channel.append(maskImg[i, j, 0])
                G_channel.append(maskImg[i, j, 1])
                B_channel.append(maskImg[i, j, 2])
                # print(maskImg[i, j, 2], type(maskImg[i, j, 2]))
    np.save(os.path.join(write_path, 'R_channel.npy'), R_channel)
    np.save(os.path.join(write_path, 'G_channel.npy'), G_channel)
    np.save(os.path.join(write_path, 'B_channel.npy'), B_channel)

    plt.figure(img_name + 'hist')
    # _ = plt.hist(maskImg.ravel(), bins = 256, color = 'orange', )
    # _ = plt.hist(maskImg[:, :, 0].ravel(), bins = 256, color = 'red', alpha = 0.5)
    # _ = plt.hist(maskImg[:, :, 1].ravel(), bins = 256, color = 'Green', alpha = 0.5)
    # _ = plt.hist(maskImg[:, :, 2].ravel(), bins = 256, color = 'Blue', alpha = 0.5)
    _ = plt.hist(R_channel, bins = 256, color = 'red', alpha = 0.5)
    _ = plt.hist(G_channel, bins = 256, color = 'Green', alpha = 0.5)
    _ = plt.hist(B_channel, bins = 256, color = 'Blue', alpha = 0.5)
    _ = plt.xlabel('Intensity Value')
    _ = plt.ylabel('Count')
    _ = plt.legend(['Red_Channel', 'Green_Channel', 'Blue_Channel'])
    plt.savefig(os.path.join(write_path, 'RGBhist.png'))
    plt.close()
    print(k, img_name)