import cv2 as cv

img = cv.imread('Resources/Photos/group 1.jpg')

cv.imshow('boston',img)

#Converting to grayscale
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Gray',gray)

#blur
blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

#Edge Cascade
#Finding Edges
canny = cv.Canny(blur,125,175)
cv.imshow('canny',canny)

#Dilating the image5
dilated = cv.dilate(canny,(7,7),iterations=5)
cv.imshow('dikated',dilated)

#Eroding
eroded = cv.erode(dilated,(7,7),iterations=5)
cv.imshow('eroded',eroded)

#Resize
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resized',resized)

#cropping
cropped = img[50:200,200:400]
cv.imshow('cropped',cropped)
cv.waitKey(0)