import cv2
import numpy as np

def sampleImage(inimg,samplingRatio):
    gray = cv2.imread(inimg,0) #0 for grayscale
    height,width=gray.shape[:2]
    blank = np.zeros((height,width), dtype = np.uint8) #create blank img for sampled pixels
    #variables
    edge = height/samplingRatio
    var = int(edge)
    xRange = var
    yRange = var
              
    xBegin = yBegin = 0
    xSeq = ySeq = 1
    
    gSeq=Sum=0
    part=samplingRatio
    
    while gSeq < part**2 :
        for i in range(xBegin,xRange):
            for j in range(yBegin,yRange):
                Sum=Sum+gray[i,j]
                
        Avg=Sum/(var**2)
        
        for x in range(xBegin,xRange):
            for y in range(yBegin,yRange):
                blank[x,y]=Avg
        
        xBegin=xSeq*var
        xRange=var+xSeq*var
        
        xSeq += 1
        Sum=0
        gSeq += 1

        
        if(xSeq==samplingRatio+1):
            xSeq=1
            xBegin=0
            xRange=var
            yBegin=ySeq*var
            yRange=var+(ySeq*var)
            ySeq += 1
        
    cv2.imshow('Sampled Image',blank)
            

