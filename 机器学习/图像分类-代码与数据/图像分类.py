#直方图均衡化
import cv2
import numpy as npy
import numpy as np
pic1=cv2.imread("./1.jpg")

#特征提取
def getfetures(img):
    thisimg=cv2.imread(img)
    thisimg=cv2.resize(thisimg,(1024,1024))
    thisimg_gray=cv2.cvtColor(thisimg,cv2.COLOR_BGR2GRAY)
    thisimg_gray=cv2.equalizeHist(thisimg_gray)
    star=cv2.xfeatures2d.StarDetector_create()
    point1=star.detect(thisimg_gray)
    sift=cv2.xfeatures2d.SIFT_create()
    point2,features=sift.compute(thisimg_gray,point1)
    return features

#批量加载各图片的特征值
cat_path="./cat/"
dog_path="./dog/"
import os
tz_all=[]
cat_allfile=os.listdir(cat_path)
for i in cat_allfile:
    thisimg=cat_path+str(i)
    cat_tz=getfetures(thisimg)
    tz_all.extend(cat_tz)
dog_allfile=os.listdir(dog_path)
for i in dog_allfile:
    thisimg=dog_path+str(i)
    dog_tz=getfetures(thisimg)
    tz_all.extend(dog_tz)
#做统一的聚类
from sklearn.cluster import KMeans
kmeans=KMeans(32)
key_tz=kmeans.fit(tz_all)
cent=key_tz.cluster_centers_
#训练
#加载猫的特征
label=[]

#新特征转换函数
def get_features(img):
    thisimg=getfetures(img)
    labels=kmeans.predict(thisimg)
    feature_vector=np.zeros(32)
    for i, item in enumerate(thisimg):
        #print("i:"+str(i))
        #print("item"+str(item))
        feature_vector[labels[i]] += 1
    feature_vector_img=np.reshape(feature_vector,((1, feature_vector.shape[0])))
    return feature_vector_img
cat_allfile=os.listdir(cat_path)
dog_allfile=os.listdir(dog_path)
all_tz=[]
all_lb=[]
for i in cat_allfile:
    thisimg=cat_path+str(i)
    cat_tz=get_features(thisimg)
    all_tz.append(cat_tz[0])
    all_lb.append("0")
for i in dog_allfile:
    thisimg=dog_path+str(i)
    dog_tz=get_features(thisimg)
    all_tz.append(dog_tz[0])
    all_lb.append("1")

#到此位置，转化后特征的图片已经全部加载
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier()
model.fit(np.array(all_tz),np.array(all_lb))
#测试
cs_alltz=[]
cs_path="./test/"
cs_allfile=os.listdir(cs_path)
for i in cs_allfile:
    thisimg=cs_path+str(i)
    cs_tz=get_features(thisimg)
    cs_alltz.append(cs_tz[0])
y2=model.predict(np.array(cs_alltz))
for i in y2:
    if(str(i)=="0"):
        print("猫")
    elif(str(i)=="1"):
        print("狗")

