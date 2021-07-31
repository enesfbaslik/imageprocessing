import cv2
import numpy as np
from padImage import padImage

def filterImage(inimg,filters):
    kernel = np.array(filters)
    kh,kw = kernel.shape[:2]

    gray = cv2.imread(inimg,0)
    ih,iw = gray.shape[:2]

    pad = padImage(inimg,ih+2,iw+2)
    blank = np.zeros((ih+2,iw+2), dtype = np.uint8)
    for i in range (1,ih+1):
        for j in range (1,iw+1):
            Sum = 0 
            for k in range(0,kh):
                for l in range(0,kw):
                    Sum = Sum + kernel[k,l]*pad[i+k-1,j+l-1]
            blank[i,j] = Sum/(kernel.shape[0]*kernel.shape[1])
            #print(Sum)
        

    cv2.imshow('Filtered',blank)
