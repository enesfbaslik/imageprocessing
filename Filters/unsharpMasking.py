import cv2
import matplotlib.pyplot as plt
from padImage import padImage
import numpy as np

def unsharpMasking(inimg,lowPassFilter,k):
    
    gray = cv2.imread(inimg,0)

    kernel = np.array(lowPassFilter)
    kh,kw = kernel.shape[:2]
    print(kh)
    ih,iw = gray.shape[:2]

    pad = padImage(inimg,ih+2,iw+2)
    blank = np.zeros((ih+2,iw+2), dtype = np.uint8)
    for i in range (1,ih+1):
        for j in range (1,iw+1):
            Sum = 0
            for k in range(0,kh):
                for l in range(0,kw):
                    Sum = Sum+kernel[k,l]*pad[i+k-1,j+l-1]
            blank[i,j] = int(Sum/9)
            #print(Sum)
    lap = cv2.Laplacian(pad,cv2.CV_64F)

    crop = lap[1:ih+1,1:iw+1]
   
    sharp = gray - k*crop

    cv2.imshow('Unsharp',sharp)

