import time
import cv2
face=cv2.CascadeClassifier("./haarcascade_frontalface_alt.xml")

path="./faces/train/name/"
n=300

cap=cv2.VideoCapture(0)
i=0
while True:
    ret,img=cap.read()
    img=cv2.resize(img,None,fx=1,fy=1)
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    face_area=face.detectMultiScale(img,1.5,5) # 检测人脸，如果没有检测到人脸，下面的for就不会执行喽
    for (x,y,w,h) in face_area:
        cv2.imwrite(path+str(i)+".jpg",img_gray)
        i+=1
        print("正在采集"+str(i)+"张图片")
    if(i>=n):
        break
    cv2.imshow("img",img)
    time.sleep(0.01)
    key=cv2.waitKey(1)
    if(key==ord("q")):
        break
