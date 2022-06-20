import cv2 as cv
import os,time
import HandTrackingModule as htm


wCam,hCam = 648,480
cap = cv.VideoCapture(0)


cap.set(3,wCam)
cap.set(4,hCam)

path = 'Resources'
myList = os.listdir(path)

ptime=0
overlaylist = []

myList = sorted(myList)

for imPath in myList:
    image = cv.imread(f'{path}/{imPath}')
    overlaylist.append(image)

detector = htm.handDetector(detectionCon=0.75)

tipIds = [4,8,12,16,20]

while True:
    success,img = cap.read()
    img = detector.findHands(img)

    lmlist = detector.findPosition(img,draw=False)
    if len(lmlist):
        fingers = []
        if lmlist[tipIds[0]][1] > lmlist[tipIds[0]-1][1]:
            fingers.append(1)

        # elif lmlist[tipIds[0]][1] < lmlist[tipIds[0]-1][1]:
        #     fingers.append(1)
        else:
            fingers.append(0)

        for id in range(1,5):
            if lmlist[tipIds[id]][2] < lmlist[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        totalfingers = fingers.count(1)

        h,w,c = overlaylist[totalfingers-1].shape
        img[0:h,0:w]= overlaylist[totalfingers-1]
        cv.rectangle(img,(10,225),(150,425),(0,255,0),cv.FILLED)
        cv.putText(img,str(totalfingers),(35,375),cv.FONT_HERSHEY_COMPLEX,5,(255,0,0),25)


    ctime =time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    cv.putText(img,str(int(fps)),(550,70),cv.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
    
    cv.imshow('Image',img)
    cv.waitKey(1)