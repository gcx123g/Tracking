import time
import jpeg4py as jpeg
import cv2
import numpy as np
from PIL import Image
import os

path = 'G:/data/GOT-10K/train/GOT-10k_Train_000001/'
image_list = os.listdir(path)

time_start = time.time()
image = [cv2.resize(cv2.imread(path+img), (256, 256)) for img in image_list]
time_end = time.time()
time_c = time_end - time_start
print('time cost', time_c, 's')


time_start = time.time()
image1 = [np.array(Image.open(path+img).resize((256, 256))) for img in image_list]
time_end = time.time()
time_c = time_end - time_start
print('time cost', time_c, 's')

a = image[1]
b = image1[1]
print(1)