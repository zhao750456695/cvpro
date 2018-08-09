# -*- coding:utf-8 -*-
import pandas as pd
from numpy import *
import numpy as np
import  operator
from os import listdir
import time
from sklearn import preprocessing

# ====== 导入数据
path = "./iris.csv"
df = pd.read_csv(path, encoding="gbk", header=None)
data = df
# =========================================================================================

# ====== 数据预处理
# 将数据转化成矩阵形式
x = df.iloc[:, 0:4].as_matrix()
y = df.iloc[:, 4].as_matrix()
# 归一化
sx = preprocessing.scale(x)
# 标准化
nx = preprocessing.normalize(x)
# ============================================================================================

# ====== 切分数据为训练集与测试集
from sklearn.model_selection import train_test_split
# 70%设为训练集，30%设为测试集
X_train, X_test, y_train, y_test = train_test_split(nx, y, test_size= .3, random_state=0)
# ==============================================================================================

# ====== KNN算法
def knn(k, traindata, y_train):
    traindatasize = traindata.shape[0]  # 训练数据第一维，代表多少行，即多少个训练数据
    result = []
    for i in range(0, len(X_test)):
        dif = np.tile(X_test[i,:], (traindatasize, 1)) - traindata
        sqdif = dif**2
        # axis=1 横向相加，即每行的和
        sumsqdif = sqdif.sum(axis=1)
        distance = sumsqdif**0.5  # 开方
        sortdistance = distance.argsort()
        count = {}
        # 前k个数据出现的各个类别
        for m in range(0, k):
            vote = y_train[sortdistance[m]]
            count[vote] =count.get(vote, 0)+1
        sortcount = sorted(count.items(), key=operator.itemgetter(1), reverse=True)
        #print("预测值："+sortcount[0][0])
        result.append(sortcount[0][0])
    return result

# 用测试数据调用KNN算法去测试，看是否能准确识别
def datatest(k):
    print("您正在使用KNN算法")
    n1 = 0
    n2 = 0
    time1 = time.time()
    for i in range(0, len(X_test)):
        n1=n1+1
        if( y_test[i] == knn(k,  X_train, y_train)[i]):
                n2+=1
        time2 = time.time()
    print("========================")
    print("KNN耗时："+str(time2-time1)+"秒")
    print("KNN错误率："+str(1-n2/n1))
    ktime = time2 - time1
    kerror_rate = 1-n2/n1
    return ktime,kerror_rate
"""
for k in range (1,20):
    datatest(k)
k = 2 为佳
下面用knn（2）
"""
# =========================================================================================

# ====== 贝叶斯算法
class Bayes:
    # 初始化属性
    def __init__(self):
        self.length = -1
        self.labelcount = dict()
        self.vectorcount = dict()
    # 训练
    def fit(self, dataSet: list, labels: list):
        print("训练开始")
        if len(dataSet) != len(labels):  # 即每个数据都有一个类别
            raise ValueError("测试数组跟类别数组长度不一致")
        self.length = len(dataSet[0])  # 测试数据特征值的长度 各个特征向量里有多少特征
        labelsnum = len(labels)  # 类别所有的数量（可重复）
        norlabels = set(labels)  # 不重复类别的数量
        for item in norlabels:  # 计算p(c)
            thislabel = item
            self.labelcount[thislabel] = labels.count(thislabel) / labelsnum
            # labels就是所有数据的类别
        for vector, label in zip(dataSet, labels):
            if (label not in self.vectorcount):
                self.vectorcount[label] = []
            self.vectorcount[label].append(vector)
        print("训练结束")
        return self

    # 测试过程
    def btest(self, TestData, labelsSet):  # 测试数据，类别集合
        if (self.length == -1):
            raise ValueError("还木有进行训练，请先训练")
        # 计算testdata分别为各个类别的概率
        lbDict = dict()
        for thislb in labelsSet:
            p = 1  # 初始化
            alllabel = self.labelcount[thislb]  # 当前类别的概率p(c)
            allvector = self.vectorcount[thislb]  # 当前类别的所有特征向量,是个列表
            vnum = len(allvector)  # 当前类别特征向量个数
            allvector = np.array(allvector).T  # 转置一下
            for index in range(0, len(TestData)):  # 依次计算各特征的概率， 特征向量有多少维就循环多少次
                vector = list(allvector[index])
                p =p* vector.count(TestData[index]) / vnum  # 当前特征数量/全部特征向量个数（即有多少个行记录）
            lbDict[thislb] = p * alllabel  # allllabel相当于p(c)
        thislabel = sorted(lbDict, key=lambda x: lbDict[x], reverse=True)[0]
        return thislabel
# ===================================================================================================================

if __name__ == '__main__':
# ====== 运用KNN算法
    ktime, kerror_rate = datatest(2)
# ====== 运用贝叶斯算法
    print("************************************")
    print("下面我们将使用贝叶斯算法")
    print("=======================")
    time1 = time.time()
    bys = Bayes()
    # 训练数据
    bys.fit(X_train.tolist(), y_train.tolist())
    # 测试
    labelsall = ['setosa', 'virginica', 'versicolor']

    num = len(y_test)
    x=0
    for i in range(0, num):
        label = bys.btest(X_test.tolist()[i], labelsall)
        print("类别是：" + str(y_test[i])+",识别出来的类别是："+str(label))
        if(label!=y_test[i]):
            x=x+1
            print("此次出错")
    time2 = time.time()
    btime = time1-time1
    berror_rate = float(x)/float(num)
    print("=======================")
    print("贝叶斯耗时：" + str(time2 - time1) + "秒")
    print("贝叶斯错误率是："+str(float(x)/float(num)))
    # a =knn(2, X_train, y_train)[2]
    # print("a:"+a)
# ====== 模型初步评估与筛选结果
    print(">>>>>>>>>>算法比较>>>>>>>>>>>")
    if ktime < btime:
        print("KNN算法耗时小,KNN好")
    else:
        print("贝叶斯算法耗时小，贝叶斯好")
    if kerror_rate < berror_rate:
        best = "KNN"
        print("KNN算法错误率低，KNN好")
    else:
        best = "贝叶斯"
        print("贝叶斯错误率低，贝叶斯好")
    print(">>>>>>>>>>算法选择>>>>>>>>>>>")
    print("我们最终的选择是：   "+best)
    print("原因描述见程序最后注释")
"""
                              模型初步评估与筛选结果
    对于尾花数据进行自动分类问题，我们最好的选择是KNN，虽然贝叶斯在时间上有优势，但对于我们当前的样本来说可以忽略
不计，我们还是倾向于选择准确率最好的算法。
    KNN耗时多的原因是：在datatest（）里面，我们使用循环：
     for i in range(0, len(X_test)):
        n1=n1+1
        if( y_test[i] == knn(k,  X_train, y_train)[i]):
                n2+=1
        time2 = time.time()
    导致knn被多次调用增加了我们的计算量。
    贝叶斯错误率高的原因是数据量太小。
"""