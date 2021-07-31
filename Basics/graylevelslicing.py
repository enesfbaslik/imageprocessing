import cv2
import numpy as np


def graylevelslicing(inimg, beginingPoint, finishPoint, resultLevel):

    gray = cv2.imread(inimg,0)
    height, width = gray.shape[:2]
    blank = np.zeros((height,width), dtype = np.uint8)

    for i in range (height):
        for j in range (width):
            if((gray[i,j] >= beginingPoint) & (gray[i,j] <= finishPoint)):
                blank[i,j]=resultLevel
            else:
                blank[i,j]=0
                
    cv2.imshow('Gray Level Sliced',blank)

            

