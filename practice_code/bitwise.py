import cv2 as cv
()
import numpy as np

blank = np.zeros((400,400),dtype='uint8')

rectangle = cv.rectangle(blank.copy(),(30,30),(370,370),255,-1)
circle = cv.circle(blank.copy(),(200,200),200,255,-1)

cv.imshow('rectangle',rectangle)
cv.imshow('circle',circle)

#bitwise and --- intersecting regions
bitwise_and = cv.bitwise_and(rectangle,circle)
cv.imshow('bitwise and',bitwise_and)

#or - intersecting and non intersecting
bitwise_or = cv.bitwise_or(circle,rectangle)
cv.imshow('bitwise or',bitwise_or)


#ex-or - non intersecting
bitwise_exor = cv.bitwise_xor(circle,rectangle)
cv.imshow('bitwise or',bitwise_exor)

#bitwise n
# ot

bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('bitwise or',bitwise_not)

cv.waitKey(0)
