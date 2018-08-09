import os
import cv2
from sklearn import preprocessing
import numpy as npy
import time
#加载训练图片的地址与类别
imgpath=[]
labels=[]
path="./faces/train/"
allperson=os.listdir(path)
for i in allperson:
    thisperson=os.listdir(path+str(i))
    for j in thisperson:
        thisimg=path+str(i)+"/"+str(j)
        imgpath.append(thisimg)
        labels.append(str(i))
#类别数字化
plabel=preprocessing.LabelEncoder()
plabel.fit(labels)
intlabels=[int(plabel.transform([i])[0]) for i in labels]
'''[a,b,c,d]'''
#加载图片
train_img=[]
train_labels=[]
face=cv2.CascadeClassifier("./haarcascade_frontalface_alt.xml")
n=0
for i in imgpath:
    img=cv2.imread(i)
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_area=face.detectMultiScale(img_gray,1.5,5)
    for (x,y,w,h) in face_area:
        thisface=img_gray[y:y+h,x:x+w]
        train_img.append(thisface)
        thislabel=intlabels[n]
        train_labels.append(thislabel)
    n+=1
#做训练
train_labels=npy.array(train_labels)
#建立人脸识别对象
'''
LBP
eigenface
fisherface
'''
rec=cv2.face.LBPHFaceRecognizer_create()
rec.train(train_img,train_labels)
#做识别
path2="./faces/test/"
alltests=os.listdir(path2)
font = cv2.FONT_HERSHEY_TRIPLEX
for i in alltests:
    thisimg=path2+str(i)
    img=cv2.imread(thisimg)
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_area=face.detectMultiScale(img,1.5,5)
    for (x,y,w,h) in face_area:
        rst,b=rec.predict(img_gray[y:y+h,x:x+w])
    #转文字
    rst2=plabel.inverse_transform([rst])[0]
    print(i)
    print("这个人是："+str(rst2))
    #cv2.putText(
    cv2.putText(img, str(rst2),(20,20), font, 1, (0, 0, 255), 1,False)
    cv2.imshow("img",img)
    cv2.waitKey(1)
    time.sleep(3)
    



 
