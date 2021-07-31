from padImage import padImage
from cropImages import cropImages
from filterImage import filterImage
from orderStFiltering import orderStFiltering
from unsharpMasking import unsharpMasking

inimg = 'F14.tif'

padImage(inimg,640,800)
cropImages(inimg,[200,200,400,400])
filterImage(inimg,[[-1,0,1],[-1,0,1],[-1,0,1]])
#filterImage(inimg,[[-1,-1,-1],[0,0,0],[1,1,1]])
#filterImage(inimg,[[0,1,0],[1,-4,-1],[0,1,0]])
#filterImage(inimg,[[0.233,0.106,0.233],[0.106,0.421,0.106],[0.233,0.106,0.233]])
#filterImage(inimg,[[1/9,1/9,1/9],[1/9,1/9,1/9],[1/9,1/9,1/9]])

#orderStFiltering(inimg, 5, 1)
#orderStFiltering(inimg, 5, 2)
orderStFiltering(inimg, 5, 3)


unsharpMasking(inimg, [[-1,-1,1],[-1,8,-1],[-1,-1,-1]], 0.3)
