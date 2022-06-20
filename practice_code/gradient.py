import cv2 as cv
import numpy as np
from yaml import DirectiveToken

#edge detection

img = cv.imread('Resources/Photos/cats.jpg')
cv.imshow('cats',img)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
#Laplacian edges
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))

#sobel
#compuutes gradient in two Direction

sobelx = cv.Sobel(gray,cv.CV_64F,1,0)
sobely = cv.Sobel(gray,cv.CV_64F,0,1)

combined_sobel = cv.bitwise_or(sobelx,sobely)

cv.imshow('sobelx',sobelx)
cv.imshow('sobely',sobely)
cv.imshow('combined sobel',combined_sobel)
cv.imshow('lap',lap)

canny = cv.Canny(gray,150,175)
cv.imshow('canny',canny)
#canny is used widely. xanny gives better and smooth edge detection image
#sobel is used in advanced past of CV. canny is used widely
cv.waitKey(0)