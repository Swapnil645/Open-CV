import cv2 as cv
from cv2 import imshow
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Resources/Photos/cats.jpg')

blank = np.zeros(img.shape[:2],dtype='uint8')
gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('gray',gray)

mask = cv.circle(blank,(img.shape[1]//2,img.shape[0]//2),100,255,-1)
cv.imshow('mask',mask)

masked = cv.bitwise_and(img,img,mask=mask)
cv.imshow('masked',masked)
#grayscale_histogram
# gray_hist = cv.calcHist([gray],[0],mask,[256],[0,256])
# plt.figure()
# plt.title('Grayscale hiostogram')
# plt.xlabel('Bins')   # interval of pixel intensity
# plt.ylabel('# of pixels')
# plt.plot(gray_hist)
# plt.xlim([0,256])
# plt.show()
# #index of image 
# cv.imshow('Cat',img)

#color hiostogram
plt.figure()
plt.title('Color hiostogram')
plt.xlabel('Bins')   # interval of pixel intensity
plt.ylabel('# of pixels')
colors=('b','g','r')
for i,col in enumerate(colors):
    hist = cv.calcHist([img],[i],mask,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)

