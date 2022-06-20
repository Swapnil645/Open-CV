import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


##### Mask and image should be of same size
img = cv.imread('Resources/Photos/cat.jpg')

cv.imshow('Cat',img)
blank = np.zeros(img.shape[:2],dtype='uint8')
cv.imshow('blank',blank)

circle = cv.circle(blank,(img.shape[1]//2 +45,img.shape[0]//2),100,255,-1)
#cv.imshow('mask',mask)

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
weird_shape = cv.bitwise_and(circle,rectangle)
#masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('weird_shape',weird_shape)
cv.waitKey(0)
