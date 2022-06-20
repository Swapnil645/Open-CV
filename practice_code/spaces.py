import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Resources/Photos/cat.jpg')

cv.imshow('Cat',img)


# plt.imshow(img)
# plt.show()
#BGR to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

#BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('hsv',hsv)

#BGR to L*a*b

lab = cv.cvtColor(img,cv.COLOR_BGR2LAB)
cv.imshow('lab',lab)


#BGR to RGB
rgb = cv.cvtColor(img,cv.COLOR_BGR2RGB)
cv.imshow('egb',rgb)
g
#HSV to BGR

hsv_bgr = cv.cvtColor(hsv,cv.COLOR_HSV2BGR)
cv.imshow('hsv_bgr',hsv_bgr)

# plt.imshow(img)
# plt.show()

cv.waitKey(0)