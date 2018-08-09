# coding=utf-8
import os
import cv2
from sklearn import preprocessing
import numpy as np
import time
from sklearn import decomposition
face = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
path = './faces/train/zhaojie/' # 请为每个人建立一个文件夹
n = 300
cap = cv2.VideoCapture(0)# 设置为0，读取摄像头
i = 0
while True:
    ret, img = cap.read()
    img = cv2.resize(img, None, fx=1, fy=1)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_area = face.detectMultiScale(img, 1.5, 5)
    for (x, y, w, h) in face_area:
        cv2.imwrite(path + str(i) + '.jpg', img_gray)
        i += 1
        print('正在采集' + str(i) + '张图片')
    if i >= n:
        break
    cv2.imshow('img', img)
    time.sleep(0.01)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break