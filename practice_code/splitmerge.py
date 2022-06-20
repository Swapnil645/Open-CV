import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np


img = cv.imread('Resources/Photos/park.jpg')

cv.imshow('Cat',img)


blank = np.zeros(img.shape[:2],dtype='uint8')


b,g,r =cv.split(img)

blue = cv.merge([b,blank,blank])
green = cv.merge([blank,g,blank])
red = cv.merge([blank,blank,r])

cv.imshow('Blue',blue)
cv.imshow('green',green)
cv.imshow('red',red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)


merged = cv.merge([b,g,r])
cv.imshow('merged',merged)
cv.waitKey(0)