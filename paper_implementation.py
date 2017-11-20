# -*- coding: utf-8 -*-
"""
Created on Sun Nov 19 20:37:28 2017

@author: Abhay KAgalkar
"""
#sin(50t)+sin(100t)+sin(200t)+sin(178.8)+sin(153.1t)
import matplotlib.pyplot as plt
import scipy
import math
#from scipy.signal import argrelextrema
#from scipy.interpolate import CubicSpline as CSP
import numpy as np
from pyhht import EMD
from pyhht.visualization import plot_imfs
f=[50,100,200,178.8,153.1]
Fs =1000
x=np.arange(0,1000)
y=np.sin(2* np.pi *f[0]*x/Fs)+np.sin(2*np.pi *f[1]*x/Fs)+np.sin(2*np.pi *f[2]*x/Fs)+np.sin(2*np.pi*f[3]*x/Fs)+np.sin(2*np.pi*f[4]*x/Fs);
plt.plot(y)
#ext1=y[argrelextrema(y, np.greater)[0]]
#min1=y[argrelextrema(y, np.less)[0]]
##f2 = interp1d(x, y, kind='cubic')
###for i in range(len(ext1)):
##    
##
#cubicspline=CSP(x,y)
##plt.plot(f2);
#extarray=cubicspline(ext1);
#minarray=cubicspline(min1);
#larr=np.zeros(176);
#larr=larr+min1     ;
decomposer = EMD(y)
imfs = decomposer.decompose()
plot_imfs(y, imfs, x)
imf1=[]
for i in range(1000):
    imf1.append(imfs[0,i]);
    
plt.subplot(2,1,1);    
plt.plot(x,imf1); 
plt.xlabel('IMF 1')
plt.ylabel('Amplitude')
plt.show()
imf2=[]
for i in range(1000):
    imf2.append(imfs[1,i]);

plt.subplot(2,1,2);    
plt.plot(x,imf2); 
plt.xlabel('IMF 2')
plt.ylabel('Amplitude')
plt.show()  
ht=scipy.signal.hilbert(imf1)
for i in range (1000):
    imf1[i]=math.pow(imf1[i],2);
    
for i in range (1000):
    ht[i]=math.pow(ht[i],2);    
a=[]    
for i in range (1000):
    a.append(math.sqrt(imf1[i]+ht[i]));

ft=np.fft.fft(a);
#plt.subplot(2,1,1);
print('Fourier');
#plt.plot(ft);
#plt.xlabel('Frequency');
#plt.ylabel('Amplitude');
#plt.show();