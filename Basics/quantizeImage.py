import cv2
import numpy as np

def quantizeImage(inimg, q):
    gray = cv2.imread(inimg,0)
    height,width = gray.shape[:2]
    blank = np.zeros((height,width), dtype = np.uint8)

    var = height/q
    for i in range (height):
        for j in range (width):
            value = gray[i,j]/var
            roundedValue = int(value)
            blank[i,j]=var*roundedValue
            
    cv2.imshow('Quantized Image',blank)
            
 
