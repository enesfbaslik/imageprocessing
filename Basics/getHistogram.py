import numpy as np
import cv2
from matplotlib import pyplot as plt

def getHistogram (inimg, inbin):
    gray = cv2.imread(inimg,0)
    hist,bins = np.histogram(gray.flatten(),inbin,[0,256]) #bin is defined python before. so i change to inbin
    plt.hist(gray.flatten(),inbin,[0,256])
    print(hist)
    plt.xlim([0,256])
    plt.show()
   
