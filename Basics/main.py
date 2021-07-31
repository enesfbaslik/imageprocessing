#You need to opencv and numpy modules for run

from sampleImage import sampleImage
from quantizeImage import quantizeImage
from powerlawtransform import powerlawtransform
from graylevelslicing import graylevelslicing
from bitplaneslicing import bitplaneslicing

inimg = 'PEPPERS.tif'

sampleImage(inimg,32)
quantizeImage(inimg,4)
powerlawtransform(inimg,0.5)
graylevelslicing(inimg, 75, 185, 240)
bitplaneslicing(inimg, 7)
 
