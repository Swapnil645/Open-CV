import cv2 as cv
import time
import poseModule
cap =  cv.VideoCapture('Resources/1.mp4')

ptime=0
detector = poseModule.poseDetector()
while True:
    success,img = cap.read()
    resized_img = detector.findPose(img)
    lmlist = detector.findPosition(resized_img)
    print(lmlist)
    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv.putText(resized_img,str(int(fps)),(70,50),cv.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)
    cv.imshow('image',resized_img)
    cv.waitKey(1)