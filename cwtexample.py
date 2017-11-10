import pywt
import numpy as np
import matplotlib.pyplot as plt
x = np.arange(300)
y = np.sin(2*np.pi*x/32)
plt.plot(x,y)
plt.show()
coef, freqs=pywt.cwt(y,np.arange(1,200),'gaus1')
plt.matshow(coef) 
plt.show() 


t = np.linspace(-1, 1, 1000, endpoint=False)
plt.plot(t)
plt.show()

sig  = np.cos(2 * np.pi * 7 * t) + np.real(np.exp(-7*(t-0.4)**2)*np.exp(1j*2*np.pi*2*(t-0.4)))
plt.plot(sig)
plt.show()

widths = np.arange(1, 100) #縦軸分解能

plt.plot(widths)
plt.show()

cwtmatr, freqs = pywt.cwt(sig, widths, 'mexh')
plt.imshow(cwtmatr, extent=[-1, 1, 1, 31], cmap='PRGn', aspect='auto',
vmax=abs(cwtmatr).max(), vmin=-abs(cwtmatr).max())  
plt.show() 