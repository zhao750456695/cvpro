import socket
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
def answer(question,address):
    #加载待计算的问题
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
        h="请输入您的身高，单位默认为cm:"
        sock.sendto(h.encode("utf-8"),address)
        thisdata,address2=sock.recvfrom(2048)
        h=thisdata.decode("utf-8")
        w="请输入您的体重，单位默认为kg:"
        sock.sendto(w.encode("utf-8"),address2)
        thisdata,address2=sock.recvfrom(2048)
        w=thisdata.decode("utf-8")
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
        thisrst="根据您的身高与体重，我们给您推荐的衣服尺寸是"+str(cm)+"，购物愉快！"
        sock.sendto(thisrst.encode("utf-8"),address2)
        return thisrst,address,1
    return answer,address,0
port=int(input("请输入您想绑定的主机端口:"))
#绑定
#socket.socket(通信方式,套接字类型)
sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
ip=""
sock.bind((ip,port))
#监听连接
#循环监控连接
while True:
    #接收连接
    thisdata,address=sock.recvfrom(2048)
    keywd=thisdata.decode("utf-8")
    #响应信息
    rst,address,issend=answer(keywd,address)
    if(issend==0):
        sock.sendto(rst.encode("utf-8"),address)
sock.close()
