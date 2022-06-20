import cv2 as cv

# img = cv.imread('Resources/Photos/cat_large.jpg')

# cv.imshow('Cat',img)


##Reading Videos
capture = cv.VideoCapture('Resources/Videos/dog.mp4')

#0,1,2,3 if webcam,camera is connected
# 0 - webcam
# 1 - cam1
# 2 - cam2 

while True:
    isTrue,frame = capture.read()
    cv.imshow('Video',frame)

    if cv.waitKey(20) and 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()


cv.waitKey(0)   #keyboard binding fucnction. waits for the key to be pressed