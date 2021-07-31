import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('circle.jpg',0) 

img_float32 = np.float32(image) 

dft = cv2.dft(img_float32, flags = cv2.DFT_COMPLEX_OUTPUT) 
dft_shift = np.fft.fftshift(dft) 

magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1])) 

fig, (ax1, ax2) = plt.subplots(nrows=1, ncols=2)

ax1.imshow(image, cmap = 'gray')
ax1.set_title('Input Image')
ax1.set_xticks([])
ax1.set_yticks([])

ax2.imshow(magnitude_spectrum, cmap = 'gray')
ax2.set_title('Magnitude Spectrum')
ax2.set_xticks([])
ax2.set_yticks([])

fig.savefig("circleresult.jpg")
