import cv2 as cv
import numpy as np

img = cv.imread('Resources/Photos/cat.jpg')

cv.imshow('cat',img)

#translation
def translate(img,x,y):
    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1],img.shape[0])
    return cv.warpAffine(img,transMat,dimensions)

# -x --> left
# -y --> Up
# x --> right
# y --> down

translated = translate(img,100,-100)
cv.imshow('translated cat',translated)

#rotation
def rotatee(img,angle,rotPoint=None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2,height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint,angle,1.0)
    dimensions = (width,height)
    return cv.warpAffine(img,rotMat,dimensions)

rotated = rotatee(img,45)
cv.imshow('roatted',rotated)

#resize
#shrinking the image - Inter_area
#enlarging - Inter_linear or Inter_cubic(high quality)
resized = cv.resize(img,(500,500),interpolation=cv.INTER_CUBIC)
cv.imshow('resize',resized)

#flip
# 0 - vertically
# 1 - horizontally
#-1 - both
flip = cv.flip(img,-1)
cv.imshow('flip',flip)

#cropping
cropped = img[200:400,400:500]
cv.imshow('cropped',cropped)

cv.waitKey(0)
