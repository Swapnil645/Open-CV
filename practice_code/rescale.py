import cv2 as cv

img = cv.imread('Resources/Photos/cat_large.jpg')

cv.imshow('Cat',img)


##Reading Videos


def rescaleFrame(frame,scale=.75):
    #works for everything
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimension = (width,height)
    return cv.resize(frame,dimension, interpolation=cv.INTER_AREA)

resized_img = rescaleFrame(img)
cv.imshow('resized_img',resized_img)

def changeRes(width,height):
    #only works for live video
    capture.set(3,width)
    capture.set(4,height)
    
capture = cv.VideoCapture('Resources/Videos/dog.mp4')


while True:
    isTrue,frame = capture.read()

    frame_resized = rescaleFrame(frame)
    cv.imshow('Video',frame)
    cv.imshow('Video Resized',frame_resized)

    if cv.waitKey(20) and 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
cv.waitKey(0)