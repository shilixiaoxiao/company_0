# -*- coding: utf-8 -*-

import cv2 as cv
import numpy as np

img_org = cv.imread(r"D:\20171210210230.jpg")  # 读入一副图像，其中包括alpha的值  imread_unchanged
gray_img = cv.cvtColor(img_org,cv.COLOR_BGR2GRAY)

kernel_x = np.zeros((3,3),float)
kernel_x[1,2] = -1.0
kernel_x[1,1] = 1.0

kernel_y = np.zeros((3,3),float)
kernel_y[1,1] = 1.0
kernel_y[2,1] = -1.0

smd_x = cv.filter2D(gray_img,-1,kernel_x)
smd_y = cv.filter2D(gray_img,-1,kernel_y)

smd_x = cv.multiply(smd_x,smd_x)
smd_y = cv.multiply(smd_y,smd_y)

G = smd_x + smd_y
G_math = cv.mean(G)[0]
print(G_math)

