import cv2 as cv

img = cv.imread('Resources/Photos/cats.jpg')

cv.imshow('Cats',img)

#thresholding - binarisation of image
# pixels - 0 or black 
#         255 or white

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)
#simple thresholding

threshold, thresh = cv.threshold(gray,150,255,cv.THRESH_BINARY)
cv.imshow('thresh',thresh)


threshold, thresh_rev = cv.threshold(gray,150,255,cv.THRESH_BINARY_INV)
cv.imshow('thresh_rev',thresh_rev)

#adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_MEAN_C,cv.THRESH_BINARY,11,9)
cv.imshow('adaptive_thresh',adaptive_thresh)

cv.waitKey(0)