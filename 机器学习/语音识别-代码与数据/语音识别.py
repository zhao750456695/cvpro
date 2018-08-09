import os
import librosa
from librosa.feature import mfcc
import numpy as npy
from hmmlearn import hmm
def getmfcc(filepath,label):
    filename=os.listdir(filepath)
    x=npy.array([])
    allwavs = []  
    alllabels = []
    for i in range(0,len(filename)):  
        wav, sr = librosa.load(filepath+"/"+filename[i], mono=True)  
        mfcc = npy.transpose(librosa.feature.mfcc(wav, sr), [1,0])  
        allwavs.append(mfcc.tolist())  
        alllabels.append(label)
    #找到最大长度
    maxlen = 0  
    for file in filename:  
        wav, sr = librosa.load(filepath+"/"+file, mono=True)  
        mfcc = npy.transpose(librosa.feature.mfcc(wav, sr), [1,0])  
        if len(mfcc) > maxlen:  
            maxlen = len(mfcc)
    #空余部分补0
    for mfcc in allwavs:  
        while len(mfcc) < maxlen:  
            mfcc.append([0]*20)
        if len(x) == 0:
            x=npy.array(mfcc)
        else:
            x=npy.concatenate((x,npy.array(mfcc)),axis=0)
    return x,alllabels

#隐马尔科夫模型是非监督学习（训练时不保存也不需要y）
class HMM(object):
    def __init__(self):
        self.allmodel=[]
        self.model = hmm.GaussianHMM(n_components=4,covariance_type='diag', n_iter=1000)
    def train(self,x):
        thismodel=self.model.fit(x)
        self.allmodel.append(thismodel)
    def rst(self,data):
        thisscore=self.model.score(data)
        return thisscore

    
traindataall="./data/"
hmm_models=[]
allfolder=os.listdir(traindataall)
for folder in allfolder:
    myhmm=None
    thisfolder=traindataall+str(folder)
    label=folder
    x=npy.array([])
    y=[]
    allfile=os.listdir(thisfolder)
    for file in allfile:
        x,y=getmfcc(thisfolder+"/",label) # 提取mfcc特征
    myhmm= HMM()
    myhmm.train(x)
    hmm_models.append((myhmm,label))

tests = ['./orange14.wav',"./apple.wav"]
for file in tests:
    wav, sr = librosa.load(file, mono=True)  
    mfcc= npy.transpose(librosa.feature.mfcc(wav, sr), [1,0])
    max_score = -10000
    rst = 0
    for thishmm in hmm_models:
        myhmm,label= thishmm
        score = myhmm.rst(mfcc)
        #print(score)
        if score > max_score:
            max_score = score
            rst = label
    print(rst)
