# coding=utf-8

import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
import time

def smd_calc(img):
    img_org = img  # 读入一副图像，其中包括alpha的值  imread_unchanged
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

    return G_math

cap = cv.VideoCapture(0)
cap.set(3,1280)
cap.set(4,720)
w = int(cap.get(3))
h = int(cap.get(4))
#print(w,h)

i = cap.get(15)         #获取曝光参数
i = -4                #修改曝光参数
cap.set(15,i)

ax = []
ay = []
plt.ion()
G_number = 0

while(cap.isOpened()):
    ret,frame = cap.read()
    cv.imshow('FullScreen', frame)
    G_math = smd_calc(frame)
    print(G_math)

    ax.append(G_number)
    ay.append(G_math)
    plt.clf()
    plt.plot(ax,ay)
    plt.pause(0.05)
    plt.ioff()
    G_number +=1

    if cv.waitKey(1) & 0xff == ord('1'):
        nowTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        print(nowTime)
        break

cap.release()
cv.destroyAllWindows()