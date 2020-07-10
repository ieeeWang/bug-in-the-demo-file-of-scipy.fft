# -*- coding: utf-8 -*-
"""
Created on Thu Jul  9 21:23:07 2020
The following code include A demo of scipy.fft, from:
    https://docs.scipy.org/doc/scipy/reference/tutorial/fft.html#d-discrete-fourier-transforms
    But, This demo of scipy has a small bug: f-axis miss the median point of the symmetrical spectrum,
    so that it will has a very tiny shift of frequency (e.g., <0.001 Hz).
    The correct demo is shown here.
@author: lwang
"""
import numpy as np
from scipy.fft import fft
import matplotlib.pyplot as plt


# Number of sample points
N = 2000
# sample spacing
T = 1.0 / 2000.0
x = np.linspace(0.0, N*T, N)
f1, f2 = 400, 420
y = np.sin(f1 * 2.0*np.pi*x) + 0.5*np.sin(f2 * 2.0*np.pi*x)
plt.figure(figsize=(16,9))
plt.plot(x, y)
plt.grid()
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Signals in the time domain')
plt.show()


yf = fft(y)

#%% demo (below) of scipy has a small bug: f-axis miss one point, 
# i.e.,the median point of the symmetrical spectrum 
xf_demo = np.linspace(0.0, 1.0/(2.0*T), N//2)
yf2_demo = 2.0/N * np.abs(yf[0:N//2])

#%% correct demo as below, note: 1+(N//2)
xf = np.linspace(0.0, 1.0/(2.0*T), 1+(N//2))
yf2 = 2.0/N * np.abs(yf[0: 1+(N//2)])

#%%
plt.figure(figsize=(10,8))
plt.plot(xf, yf2, label='corrected demo')
plt.plot(xf_demo, yf2_demo, '--',label='demo')
plt.grid()
plt.xlim((350,450))
plt.legend(loc='best', fontsize='x-large')
plt.xlabel('f (Hz)')
plt.ylabel('|y(f)|')
plt.title('Signals in the frequency domain')
plt.show()


plt.figure(figsize=(16,9))
plt.plot(np.abs(yf))
plt.title('The symmetrical FT spectrum')


