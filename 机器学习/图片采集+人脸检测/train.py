# coding=utf-8
import os
import cv2
from sklearn import preprocessing
import numpy as np
import time
from sklearn import decomposition
import pymysql
import pickle

# 加载训练图片的地址与类别
imgpath =[]
labels = []
path = './faces/train/'
allperson = os.listdir(path)
for i in allperson:
    thisperson = os.listdir(path + str(i))
    for j in thisperson:
        thisimg = path + str(i) +'/' +str(j)
        imgpath.append(thisimg)
        labels.append(str(i))

# 类别的数字化
plabel = preprocessing.LabelEncoder()
plabel.fit(labels)
intlabels = [int(plabel.transform([i])[0]) for i in labels ]
# 加载图片
train_img = []
train_labels = []
face = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
n = 0
for i in imgpath:
    img = cv2.imread(i)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_area = face.detectMultiScale(img_gray, 1.5, 5)
    for (x, y, w, h) in face_area:
        thisface = img_gray[y:y+h, x:x+w]
        train_img.append(thisface)
        thislabel = intlabels[n]
        train_labels.append(thislabel)
    n+=1
# pca降维
train_img2 = []
for i in range(0, len(train_img)):
    pca = decomposition.PCA()
    ft1 = pca.fit(train_img[i])
    ft1 = pca.explained_variance_
    # 有效特征数估计
    ft2_num = len(np.where(ft1 > 0.6)[0])
    #print(ft2_num)
    pca.n_components = 67
    # 特征转换
    thisimgft = pca.fit_transform(train_img[i])
    train_img2.append(thisimgft)
# 做训练
train_labels = np.array(train_labels)

fh = open('plabel.pk', 'wb')
pickle.dump(plabel, fh)
fh.close()
fh = open('train_img.pk', 'wb')
pickle.dump(train_img, fh)
fh.close()
fh = open('train_img2.pk', 'wb')
pickle.dump(train_img2, fh)
fh.close()
fh = open('train_labels.pk', 'wb')
pickle.dump(train_labels, fh)
fh.close()
