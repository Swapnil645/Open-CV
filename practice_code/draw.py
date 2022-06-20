import cv2 as cv
from cv2 import circle
from cv2 import line
from matplotlib.lines import Line2D
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')   ##data type of image
#shape:height,width,number od color channels
cv.imshow('blank',blank)

#1. Paint the image 
# blank[:] = 0,255,255
# cv.imshow('painted',blank)


# #2. Draw rectangle
# cv.rectangle(blank,(0,0),(250,250),(0,255,0),thickness=-1)
# cv.imshow('painted-rectangle',blank)

# #tickness : cv.filled = -1

# #3.Draw circle
# cv.circle(blank,(blank.shape[1]//2,blank.shape[0]//2),100,(0,0,255),thickness=-1)
# cv.imshow('painted-rectangle',blank)

# #4.Draw Line
# cv.line(blank,(0,0),(blank.shape[1]//2,blank.shape[0]//2),(255,255,255),thickness=1)
# cv.imshow('painted-rectangle',blank)

#5. Write text
cv.putText(blank,'Hello',(0,255),cv.FONT_HERSHEY_TRIPLEX,1.0,(0,255,0),thickness=2)
cv.imshow('text',blank)


cv.waitKey(0)