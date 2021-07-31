import cv2
import numpy as np
from padImage import padImage

def orderStFiltering(inimg, filterSize, typeOfStatistics):
    kernel = np.zeros((filterSize,filterSize))
    kh,kw = kernel.shape[:2]
    
    gray = cv2.imread(inimg,0)
    ih,iw = gray.shape[:2]
    print(iw)
    pad = padImage(inimg,ih+(filterSize-1),iw+(filterSize-1))
    blank = np.zeros((ih+2,iw+2), dtype = np.uint8)
    offset=int((filterSize-1)/2)
    for i in range (offset,ih+offset):
        for j in range (offset,iw+offset):
            Sum = 0
            for k in range(0,kh):
                for l in range(0,kw):
                    kernel[k,l] = pad[i+k-offset,j+l-offset]
                    #print(kernel)
            if(typeOfStatistics==1):
                blank[i,j]=np.median(kernel)
            elif(typeOfStatistics==2):
                blank[i,j]=np.max(kernel)
            elif(typeOfStatistics==3):
                blank[i,j]=np.min(kernel)
                    
    cv2.imshow('St Filtered',blank)
    return blank

