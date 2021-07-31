from histogramEqualization import histogramEqualization
from getHistogram import getHistogram

inimg = 'PEPPERS.tif'

getHistogram(inimg,64)
histogramEqualization(inimg)
