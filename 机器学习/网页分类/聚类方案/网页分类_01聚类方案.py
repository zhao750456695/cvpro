import os
import jieba
import pymysql
import re
import numpy as npy
import pandas as pda
from sklearn.feature_extraction.text import CountVectorizer
conn=pymysql.connect(host="127.0.0.1",user="root",passwd="root",db="iqianyue")
sql="select title,content from article limit 1000"
def loaddata(data):
    data1=jieba.cut(data)
    data11=""
    for item in data1:
        data11+=item+" "
    return data11
dataf=pda.read_sql(sql,conn)
dataf2=dataf.T
title=dataf2.values[0]
content=dataf2.values[1]
train_text=[]
for i in content:
    thisdata=loaddata(str(i))
    pat1="<[^>]*?>"
    thisdata=re.sub(pat1,"",thisdata)
    thisdata=thisdata.replace("\n","").replace("\t","")
    train_text.append(thisdata)
count_vect = CountVectorizer()
train_x_counts = count_vect.fit_transform(train_text)
#tfidf模型
from sklearn.feature_extraction.text import TfidfTransformer
tf_ts = TfidfTransformer(use_idf=True).fit(train_x_counts)
train_x_tf = tf_ts.transform(train_x_counts)
from sklearn.cluster import KMeans
kms=KMeans(n_clusters=3)
y=kms.fit_predict(train_x_tf)
dataf["type"]=y
dataf.to_csv("./01聚类归类法结果.csv")
