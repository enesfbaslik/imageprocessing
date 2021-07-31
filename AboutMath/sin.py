from matplotlib import pyplot as plt
import math
import numpy as np
import cv2

def normalize_img(s):
    start = 0
    end = 255
    width = end - start
    res = (s - s.min())/(s.max() - s.min()) * width + start
    return res

A = 0.5
f = 7
t = np.linspace(0,1,50) 
phi = np.pi/4
x = normalize_img(A*np.cos(2*np.pi*f*t + phi)) 
sinusoid = np.array([x]*len(t)).astype(np.float32) 

dft = cv2.dft(sinusoid, flags = cv2.DFT_COMPLEX_OUTPUT) 
dft_shift = np.fft.fftshift(dft) 

magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1])+1) 

fig, (ax1, ax2) = plt.subplots(figsize=(9, 5), nrows=1, ncols=2)

ax1.imshow(sinusoid, cmap = 'gray')
ax1.set_title('Sinusoid 1')
ax1.set_xticks([])
ax1.set_yticks([])

ax2.imshow(magnitude_spectrum, cmap = 'gray')
ax2.set_title('Frequency Spectrum 1')
ax2.set_xticks([])
ax2.set_yticks([])
fig.savefig('vertical.jpg')
