import time
import cv2
import numpy as np
from PIL import Image
import os

path = 'E:/data/GOT-10K/train/GOT-10k_Train_000001/'
image_list = os.listdir(path)

time_start = time.time()
image = [cv2.resize(cv2.imread(path+img), (256, 256)) for img in image_list]
time_end = time.time()
time_c = time_end - time_start
print('time cost', time_c, 's')


time_start = time.time()
image1 = [Image.open(path+img).resize((256, 256)) for img in image_list]
time_end = time.time()
time_c= time_end - time_start
print('time cost', time_c, 's')