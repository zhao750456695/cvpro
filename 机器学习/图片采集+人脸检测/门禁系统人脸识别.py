# coding=utf-8
import os
import cv2
from sklearn import preprocessing
import numpy as np
import time
from sklearn import decomposition
import pymysql
import pickle
# 链接数据库
conn = pymysql.connect(host="127.0.0.1", user="root", passwd="root", db="studentlist", charset='utf8', use_unicode=True)
cur = conn.cursor()
# 导入腌制好的数据
face = cv2.CascadeClassifier('./haarcascade_frontalface_alt.xml')
fh = open('plabel.pk', 'rb')
plabel = pickle.load(fh)
fh.close()
fh = open('train_img.pk', 'rb')
train_img = pickle.load(fh)
fh.close()
fh = open('train_img2.pk', 'rb')
train_img2 = pickle.load(fh)
fh.close()
fh = open('train_labels.pk', 'rb')
train_labels = pickle.load(fh)
fh.close()

# 基于摄像头识别
rec = cv2.face.LBPHFaceRecognizer_create()
rec.train(train_img2, train_labels)
cap = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_TRIPLEX
while True:
    ret, img = cap.read()
    img = cv2.resize(img, None, fx=1, fy=1)
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    face_area = face.detectMultiScale(img, 1.5, 5)
    for (x, y, w, h) in face_area:
        rst, b =rec.predict(img_gray[y: y+h, x: x+w])
        rst2 = plabel.inverse_transform([rst])[0]
        try:
            sql = 'select * from studentlist where name = "%s";' % rst2
            cur.execute(sql)
            result = cur.fetchall()
        except Exception as err:
            print(err)
        # 数据库中若有识别者的姓名，则可以开门。
        if result[0][1] == str(rst2):
            # 此处应触发开门开关
            try:
                sql2 = 'INSERT INTO studentrecord (name,studentid,time) VALUES ("%s", "%d",NOW());' % (result[0][1], result[0][2])
                cur.execute(sql2)
                conn.commit()
            except Exception as err:
                print(err)
            print('已经开门')
            print('这个人是：' + str(rst2))
        else:
            print('无法识别')
    cv2.imshow('img', img)
    cv2.waitKey(1)
    time.sleep(5)
    key = cv2.waitKey(1)
    if key & 0xFF == ord('q'):
        break
