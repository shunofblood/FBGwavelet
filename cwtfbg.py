import pywt
import numpy as np
import matplotlib.pyplot as plt
#import pandas as pd
#import os
import tkinter.filedialog as tkf

filename = tkf.askopenfilename(title="select csv datafile")
data = np.loadtxt(filename, comments='#', delimiter=',')


#os.chdir("C:\Users\shun\Desktop")
#df=pd.read_csv("1.csv")

#y=df
#y = np.loadtxt("C:\Users\shun\Desktop\\1.csv",delimiter="\t", usecols=(0)) #retusenntauk
#print(y)
#plt.plot(y)
#plt.show()


coef, freqs=pywt.cwt(data,np.arange(1,500),'gaus1') 
plt.matshow(coef) 
plt.show() 

t = np.linspace(-1, 1, 200, endpoint=False)
plt.plot(t)
plt.show()

#widths = np.arange(1, 100) #縦軸分解能

#sig  = np.cos(2 * np.pi * 7 * t) + np.real(np.exp(-7*(t-0.4)**2)*np.exp(1j*2*np.pi*2*(t-0.4)))
#widths = np.arange(1, 31)
#cwtmatr, freqs = pywt.cwt(df, widths, 'mexh')
#plt.imshow(cwtmatr, extent=[-1, 1, 1, 31], cmap='PRGn', aspect='auto',
#vmax=abs(cwtmatr).max(), vmin=-abs(cwtmatr).max())  
#plt.show() 