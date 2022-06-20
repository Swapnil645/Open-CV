import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cat.jpg')

cv.imshow('cat',img)

blank = np.zeros(img.shape,dtype='uint8')
cv.imshow('blank',blank)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

blur = cv.GaussianBlur(gray,(5,5),cv.BORDER_DEFAULT)

canny = cv.Canny(blur,125,175)
cv.imshow('canny',canny)

# rest,thresh = cv.threshold(gray,125,255,cv.THRESH_BINARY)  # binaring the imgae less than 125 is black and above is white
# cv.imshow('thresh',thresh)
contours, heirarachies = cv.findContours(canny,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)
print(len(contours))

contours_drawn = cv.drawContours(blank,contours,-1,(0,0,255),   1)
cv.imshow('contours_drawn',contours_drawn)
#-1 - all of them
cv.waitKey(0)