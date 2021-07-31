import numpy as np
import cv2
from matplotlib import pyplot as plt

image = cv2.imread('Fig4.21.jpg',0)

image_float32 = np.float32(image) 

dft = cv2.dft(image_float32, flags = cv2.DFT_COMPLEX_OUTPUT) 
dft_shift = np.fft.fftshift(dft) 
magnitude_spectrum = 20*np.log(cv2.magnitude(dft_shift[:,:,0],dft_shift[:,:,1]))

fig, (ax1, ax2) = plt.subplots(figsize=(9, 5), nrows=1, ncols=2)
ax1.imshow(image, cmap = 'gray')
ax1.set_title('Input Image')
ax1.set_xticks([])
ax1.set_yticks([])

ax2.imshow(magnitude_spectrum, cmap = 'gray')
ax2.set_title('Magnitude Spectrum')
ax2.set_xticks([])
ax2.set_yticks([])

rows, cols = image.shape
crow, ccol = rows//2 , cols//2


mask = np.ones((rows, cols, 2), np.uint8)
mask[crow-30:crow+30, ccol-30:ccol+30] = 0


fshift = dft_shift*mask
f_ishift = np.fft.ifftshift(fshift)
img_back = cv2.idft(f_ishift)
img_back = cv2.magnitude(img_back[:,:,0],img_back[:,:,1])

plt.subplot(121)
plt.imshow(image, cmap = 'gray')
plt.title('Input Image')
plt.axis('off')

plt.subplot(122)
plt.imshow(img_back, cmap = 'gray')
plt.title('Ringed Image')
plt.axis('off')

plt.show()
