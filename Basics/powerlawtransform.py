import numpy as np
import cv2

def powerlawtransform(inimg, power):
    
    gray = cv2.imread(inimg,0)
  
    powerImg = np.array(255*(gray/255)**power,dtype='uint8')

    cv2.imshow('Output Image',powerImg)
