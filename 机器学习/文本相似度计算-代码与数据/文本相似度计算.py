from gensim import corpora,models,similarities
from collections import defaultdict
import jieba
import urllib.request
d1=urllib.request.urlopen("http://127.0.0.1/ljm.html").read().decode("utf-8","ignore")
d2=urllib.request.urlopen("http://127.0.0.1/gcd.html").read().decode("utf-8","ignore")
'''
词语1,词语2
====》
词语1 词语2
'''
# 分词
data1=jieba.cut(d1)
data2=jieba.cut(d2)
data11=""
for item in data1:
    data11+=item+" "
data21=""
for item in data2:
    data21+=item+" "
docs=[data11,data21]
'''
[[词语1,词语2],
[词语1,词语2]]
'''
tall=[[w1 for w1 in doc.split()] for doc in docs]
#print(len(tall[1]))
# 统计词频
frequency=defaultdict(int)
for text in tall:
    for token in text:
        frequency[token]+=1

#过滤（可选）
# 词频大于25的才留下来
tall=[[token for token in text if frequency[token]>25]for text in tall]
#print(len(tall[1]))
# 建立语料库词典
dictionary=corpora.Dictionary(tall)
#dictionary.save("./novels.txt")

d3=urllib.request.urlopen("http://127.0.0.1/dmbj.html").read().decode("utf-8","ignore")
data3=jieba.cut(d3)
data31=""
for item in data3:
    data31+=item+" "
this_novels=data31
# 根据已有的语料库词典转换为词袋
new_vec=dictionary.doc2bow(this_novels.split())
# 新的语料库
corpus=[dictionary.doc2bow(text) for text in tall]
tfidf=models.TfidfModel(corpus)
num=len(dictionary.token2id.keys())
index=similarities.SparseMatrixSimilarity(tfidf[corpus],num_features=num)
sim=index[tfidf[new_vec]]
