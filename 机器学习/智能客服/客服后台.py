import jieba
import gensim
from gensim import corpora,models,similarities
import pymysql
import numpy
import pickle
import os
#直接加载训练好的模型
fh=open("modle.pk","rb")
dictionary=pickle.load(fh)
fh.close()
fh=open("index.pk","rb")
index=pickle.load(fh)
fh.close()
fh=open("tfidf.pk","rb")
tfidf=pickle.load(fh)
fh.close()
fh=open("a.pk","rb")
a=pickle.load(fh)
fh.close()
#加载待计算的问题
while True:
    question=input("请输入问题:")
    data3=jieba.cut(question)
    data31=""
    for item in data3:
        data31+=item+" "
    new_doc=data31
    new_vec=dictionary.doc2bow(new_doc.split())
    sim=index[tfidf[new_vec]]
    pos=sim.argsort()[-1]
    answer=a[pos]
    if(answer=="an01"):
        h=input("请输入您的身高，单位默认为cm:")
        w=input("请输入您的体重，单位默认为kg:")
        if(int(h)>=160 and int(h)<=170):
            if(int(w)<50):
                cm="S"
            elif(int(w)>65):
                cm="XXL"
            else:
                cm="XL"
        elif(int(h)>=170 and int(h)<=180):
            if(int(w)<65):
                cm="XL"
            elif(int(w)>85):
                cm="XXXL"
            else:
                cm="XXL"
        else:
            cm="没有符合条件尺码的衣服"
        print("根据您的身高与体重，我们给您推荐的衣服尺寸是"+str(cm)+"，购物愉快！")
        continue
    print(answer)
