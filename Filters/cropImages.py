import cv2
import numpy as np

def cropImages(inimg,cropArray):
    img = cv2.imread(inimg,0)
    array = np.array(cropArray)

    crop_img = img[array[0]:array[2], array[1]:array[3]]
    cv2.imshow("Cropped", crop_img)
    
    return crop_img
