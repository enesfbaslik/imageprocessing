import cv2
import numpy as np

def padImage(inimg,nrp,ncp):
    gray = cv2.imread(inimg, 0)
    height, width = gray.shape[:2]

    pad = np.zeros((nrp,ncp), dtype = np.uint8)
    hh, ww = pad.shape[:2]
    print(hh,ww)
   
    yoff = round((hh-height)/2)
    xoff = round((ww-width)/2)
    print(yoff,xoff)

    result = pad.copy()
    result[yoff:yoff+height, xoff:xoff+width] = gray

    # view result
    cv2.imshow('Padded Image', result)
    
    return result
