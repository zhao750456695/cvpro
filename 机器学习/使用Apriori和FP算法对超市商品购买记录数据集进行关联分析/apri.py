# -*- coding=utf-8 -*-
# import pdb
# pdb.set_trace()
import pandas as pd
def loadDataSet():
    return [[1, 3, 4], [2, 3, 5], [1, 2, 3, 5], [2, 5]]

def createC1(dataSet):
    c1 = []
    for transaction in dataSet:
        for item in transaction:
            if not [item] in c1:

                c1.append([item])
    c1.sort()
    return map(frozenset, c1)

def scanD(D, ck, minSupport):
    ssCnt = {}
    for tid in D:
        for can in ck:
            if can.issubset(tid):
                if not can in ssCnt:ssCnt[can]=1
                else:ssCnt[can] += 1
    numItems = float(len(D))
    retlist = []
    supportData = {}
    for key in ssCnt:
        support = ssCnt[key]/numItems
        if support >= minSupport:
            retlist.insert(0, key)
        supportData[key] = support
    return retlist, supportData

#dataSet = loadDataSet()

# dataSet = []
# for i in range(1, 748):
#     d1 = data.iloc[i, :].tolist()
#     d1 = [x for x in d1 if str(x) != 'nan']
#     dataSet.append(d1)
#
# print(dataSet)
def aprioriGen(lk, k):
    retlist = []
    lenlk = len(lk)
    for i in range(lenlk):
        for j in range(i+1, lenlk):
            l1 = list(lk[i])[:k - 2];l2 = list(lk[j])[:k - 2]  # [:k-2} [0:0]不取东西
            l1.sort(); l2.sort()
            if l1 == l2:
                retlist.append(lk[i]|lk[j])
    return retlist

def apriori(dataSet, minSupport = 0.4):
    c1 = list(createC1(dataSet))
    D = list(map(set, dataSet))
    L1, supportData = scanD(D, c1, minSupport)
    L = [L1]
    k = 2

    #print(L[k-2])
    while len(L[k-2]) > 0:
        ck = aprioriGen(L[k-2], k)
        lk, supk = scanD(D, ck, minSupport)
        supportData.update(supk)
        L.append(lk)
        k += 1
    return L, supportData
#l, suppdata = apriori(dataSet)

def generateRules(l, suppdata, minconf=0.7):
    bigRuleList = []
    for i in range(1, len(l)):
        for fregSet in l[i]:
            H1 = [frozenset([item]) for item in fregSet]
            if (i>1):
                rulesFromConseq(fregSet, H1, suppdata, bigRuleList, minconf)
            else:
                calcConf(fregSet, H1, suppdata, bigRuleList, minconf)
    return bigRuleList

def calcConf(freqSet, H, suppdata, brl, minConf=0.7):
    prunedH = []
    for conseq in H:
        conf = suppdata[freqSet]/suppdata[freqSet-conseq]
        if conf >= minConf:
            print(freqSet-conseq,"-->",conseq,"conf:",conf)
            brl.append((freqSet-conseq, conseq, conf))
            prunedH.append(conseq)
    return prunedH

def rulesFromConseq(freqSet, H, suppdata, brl, minConf=0.7):
    m = len(H[0])
    if (len(freqSet) > (m + 1)):
        Hmp1 = aprioriGen(H, m +1 )
        Hmp1 = calcConf(freqSet, Hmp1, suppdata, brl, minConf)
        if (len(Hmp1) > 1):
            rulesFromConseq(freqSet, Hmp1, suppdata, brl, minConf)

# rules = generateRules(l, suppdata, minconf=0.3)
# print(rules)

