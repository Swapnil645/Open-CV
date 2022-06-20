import cv2 as cv
import time
import HandTrackingModule


pTime = 0
cTime = 0
cap = cv.VideoCapture(0)
detector = HandTrackingModule.handDetector()
while True:
    success,img = cap.read()
    cTime = time.time()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img)
    if len(lmlist)!= 0:
        print(lmlist[4])
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv.putText(img,str(int(fps)),(10,70),cv.FONT_HERSHEY_COMPLEX,3,(255,0,255),2)
    cv.imshow('image',img)
    cv.waitKey(1)