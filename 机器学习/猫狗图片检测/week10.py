
import cv2
import numpy as np
import os
import time


def get_file_name(path):
    filenames = os.listdir(path)
    path_filenames = []
    filename_list = []
    for file in filenames:
        if not file.startswith('.'):
            path_filenames.append(os.path.join(path, file))
            filename_list.append(file)

    return path_filenames

"""
特征检测可以通过特征检测器实现，主要有：
1、sift特征检测
2、star_sift迭代模型检测
"""

def sift(path):
    time1 = time.time()
    print('>>>>>>>>>>现在进行sift特征检测>>>>>>>>>>>')
    pic1 = cv2.imread(path)
    pic2 = cv2.cvtColor(pic1, cv2.COLOR_BGR2GRAY)
    sift = cv2.xfeatures2d.SIFT_create()
    point = sift.detect(pic2, None)
    print('特征点个数：', len(point))
    cv2.drawKeypoints(pic1, point, pic1, flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT)
    time2 = time.time()
    d = time2 - time1
    print('耗时：', d)
    #cv2.imshow('pic12', pic12)
    #cv2.imshow('pic111',pic1)
    #cv2.waitKey(0)

"""
模型检测
"""

def star_sift(path):
    print('>>>>>>>>>>现在进行star-sift迭代模型检测>>>>>>>>>>')
    time1 = time.time()
    pic1 = cv2.imread(path)
    pic2 = cv2.cvtColor(pic1, cv2.COLOR_BGR2GRAY)
    # star-sift 迭代模型检测
    star = cv2.xfeatures2d.StarDetector_create()
    point = star.detect(pic2)
    sift = cv2.xfeatures2d.SIFT_create()
    point2, features = sift.compute(pic2, point)
    print('特征点个数：', len(point2))
    cv2.drawKeypoints(pic1, point2, pic1, flags=cv2.DRAW_MATCHES_FLAGS_DEFAULT)
    time2 = time.time()
    print('耗时：', time2-time1)
    #cv2.imshow('pic22',pic1)
    # 特征提取
    #cv2.waitKey(0)


if __name__ == '__main__':
    path = './dog/'
    path1 = './cat/'
    dog = get_file_name(path)
    cat = get_file_name(path1)

    for dog in dog:
        print(dog)
        sift(dog)
        star_sift(dog)
    for cat in cat:
        print(cat)
        sift(cat)
        star_sift(cat)