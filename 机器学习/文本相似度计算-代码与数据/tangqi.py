import jieba
import gensim
from gensim import corpora,models,similarities
import pymysql
import numpy
import os
#bookname用于存储书籍名
bookname=[]
#contentcut用于存储所有切词后的小说内容
contentcut=[]
#加载作者自己的其他小说
booklist1=os.listdir("./作者自己的其他作品")
num1=len(booklist1)
for i in booklist1:
    bookname.append(str(i))
    thiscontent=open("./作者自己的其他作品/"+str(i),"r",encoding="utf-8").read()
    data1=""
    thisdata=jieba.cut(thiscontent)
    for item in thisdata:
        data1+=item+" "
    contentcut.append(data1)
#加载不涉嫌抄袭的不同类小说
booklist2=os.listdir("./不涉嫌抄袭的不同类作品")
num2=len(booklist2)
for i in booklist2:
    bookname.append(str(i))
    thiscontent=open("./不涉嫌抄袭的不同类作品/"+str(i),"r",encoding="utf-8").read()
    data1=""
    thisdata=jieba.cut(thiscontent)
    for item in thisdata:
        data1+=item+" "
    contentcut.append(data1)
#加载不涉嫌抄袭的同类小说
booklist3=os.listdir("./不涉嫌抄袭的同类作品")
num3=len(booklist3)
for i in booklist3:
    bookname.append(str(i))
    thiscontent=open("./不涉嫌抄袭的同类作品/"+str(i),"r",encoding="utf-8").read()
    data1=""
    thisdata=jieba.cut(thiscontent)
    for item in thisdata:
        data1+=item+" "
    contentcut.append(data1)
#加载涉嫌抄袭的作品
booklist4=os.listdir("./涉嫌抄袭的作品")
num4=len(booklist4)
for i in booklist4:
    bookname.append(str(i))
    thiscontent=open("./涉嫌抄袭的作品/"+str(i),"r",encoding="utf-8").read()
    data1=""
    thisdata=jieba.cut(thiscontent)
    for item in thisdata:
        data1+=item+" "
    contentcut.append(data1)
#
docs=contentcut
tall=[[w1 for w1 in doc.split()]
		for doc in docs]
from collections import defaultdict
frequency=defaultdict(int)
for text in tall:
	for token in text:
		frequency[token]+=1

tall=[[token for token in text if frequency[token]>300]
		for text in tall]
dictionary=corpora.Dictionary(tall)
#dictionary.save('D:/Python35/deerwester.dict')
#加载待计算作品
d3=open("./待计算的主作品/三生三世十里桃花.txt","r",encoding="utf-8").read()
data3=jieba.cut(d3)
data31=""
for item in data3:
    data31+=item+" "
new_doc=data31
new_vec=dictionary.doc2bow(new_doc.split())
corpus=[dictionary.doc2bow(text) for text in tall]
#corpora.MmCorpus.serialize('D:/Python35/6562.txt',corpus) 
tfidf=models.TfidfModel(corpus)

num=len(dictionary.token2id.keys())
index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=num)
sim=index[tfidf[new_vec]]
#print(sim)
for i in range(0,num1):
    print("与作者自己的其他小说相似度:")
    for j in range(0,len(sim[0:num1])):
        print(str(bookname[0+j])+str("：")+str(sim[0+j]))
print("------------")
for i in range(0,num1):
    print("与不涉嫌抄袭的不同类小说相似度:")
    for j in range(0,len(sim[num1:num1+num2])):
        print(str(bookname[num1+j])+str("：")+str(sim[num1+j]))
print("------------")
for i in range(0,num1):
    print("与不涉嫌抄袭的同类小说相似度:")
    for j in range(0,len(sim[num1+num2:num1+num2+num3])):
        print(str(bookname[num1+num2+j])+str("：")+str(sim[num1+num2+j]))
print("------------")
for i in range(0,num1):
    print("与涉嫌抄袭的小说相似度:")
    for j in range(0,len(sim[num1+num2+num3:num1+num2+num3+num4])):
        print(str(bookname[num1+num2+num3+j])+str("：")+str(sim[num1+num2+num3+j]))

