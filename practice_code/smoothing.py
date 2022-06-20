import cv2 as cv
from cv2 import blur
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/cat.jpg')

cv.imshow('Cat',img)

average = cv.blur(img,(7,7))
cv.imshow('avg_blur',average)
#gaussian blur
gauss = cv.GaussianBlur(img,(7,7),0)
cv.imshow('gauss',gauss)

#Median Blur

median = cv.medianBlur(img,7)
cv.imshow('median',median)

#Bilateral Blur
bilateral = cv.bilateralFilter(img,10,35,25)
cv.imshow('bilateral',bilateral)
#retains the edges in the image
cv.waitKey(0)
