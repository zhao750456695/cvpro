# -*- coding=utf-8 -*-
import FP_Grow_tree
import pandas as pd
import apri
import time

"""
将原始数据中的F转为空，将T转为商品名称，形成新的excel：data666.xls，并存在当前目录下，以备使用。
# 数据预处理
data = pd.read_excel("./data.xls", encoding="utf-8")
for r in range(0, 748):
    for c in range(0, 195):
        if data.iloc[r,c]=="F":
            data.iloc[r,c]=""
        if data.iloc[r,c]=="T":
            data.iloc[r,c]=data.iloc[0,c]
data.to_excel("./data666.xls")
"""
data = pd.read_excel("./data666.xls", encoding="utf-8")
# 将交易记录变成列表的形式
dataSet = []
for i in range(1, 748):
    d1 = data.iloc[i, :].tolist()
    d1 = [x for x in d1 if str(x) != 'nan']
    dataSet.append(d1)
    #print(dataSet)


# =========================================================================================
print(">>>>>>>>>>>>>>> 使用FP_Growth_tree >>>>>>>>>>>>>>>>>>>>>")
time1 = time.time()
support=300 # 支持度设为300
ff=FP_Grow_tree.FP_Grow_tree(dataSet,[],support)
# 打印频繁集
ff.printfrequent()
time2 = time.time()
print('FP_Growth_tree耗时：', str(time2-time1))


# =======================================================================================
print(">>>>>>>>>>>>>>> 使用Apriori >>>>>>>>>>>>>>>>>>>>>")
time1 = time.time()
l, suppdata = apri.apriori(dataSet) # 对数据集使用apriori算法
print(l)
rules = apri.generateRules(l, suppdata, minconf=0.7) # 生成关联规则，最小置信度设为0.7
print(rules)
time2 = time.time()
print('Apriori耗时：',time2-time1)