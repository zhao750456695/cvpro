#语音数字化\可视化
import numpy as np
import matplotlib.pylab as plt
from scipy.io import wavfile
a,b = wavfile.read('./apple.wav') # a是频率特征，b是波形特征
b=b/(2.**15)
#时间特征
x=1000*np.arange(0, len(b), 1)/float(a)
plt.plot(x,b)
plt.show()

#MFCC
import librosa
from librosa.feature import mfcc
wav,sr=librosa.load('./apple.wav', mono=True)
mfcc = np.transpose(librosa.feature.mfcc(wav, sr), [1,0])

#傅里叶变换
f= np.fft.fft(b)
