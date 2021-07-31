import numpy as np
import cv2

#i have no idea for this code. I found it in the Internet and revised for my homework
def bitplaneslicing(inimg, bitplaneNumber):
    gray = cv2.imread(inimg,0)
    height,width = gray.shape[:2]
    lst = []
    for i in range(height):
        for j in range(width):
             lst.append(np.binary_repr(gray[i][j] ,width=8))
    coefficient = 2**(bitplaneNumber-1)
    value = 8 - bitplaneNumber
    outimg = (np.array([int(i[value]) for i in lst],dtype = np.uint8) * coefficient).reshape(height,width)

    cv2.imshow('Bitplane Sliced',outimg)
