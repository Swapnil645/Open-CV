import cv2 as cv
import numpy as np
import time

import poseModule

cap =cv.VideoCapture('Resources/8.mp4')

dir = 0
count=0
detector = poseModule.poseDetector()
ptime = 0

while(True):
    success,img = cap.read()
    #img = cv.imread('Resources/10.jpg')
    #img = poseModule.rescaleFrame(img,0.17)
   
    img = cv.resize(img,(1288,720))
    img = detector.findPose(img,False)
    lmlist = detector.findPosition(img,False)
    if len(lmlist):
        #detector.findAngle(img,12,14,16)
        #left
        angle,img = detector.findAngle(img,12,14,16)
        per = np.interp(angle,(40,180),(0,100))
       
        #check for dumbell curls
        if per == 100:
            if dir == 0:
                count +=0.5
                dir = 1
        if per == 0:
            if dir==1:
                count+=0.5
                dir=0
        if count>=2 and count<=3:
            print(count,per,angle)
        cv.putText(img,f'{int(count)}',(50,100),cv.FONT_HERSHEY_COMPLEX,5,(255,0,0),5)


    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime

    #cv.rectangle(img,(0,450),(250,720),(0,255,0),cv.FILLED)
   
    cv.putText(img,f'FPS-{str(int(fps))}',(1000,80),cv.FONT_HERSHEY_COMPLEX,1,(255,0,0),1)
    #print(lmlist)
     

    cv.imshow('image',img)
    cv.waitKey(1)




#     collaborative tools from DS perspective
# ebay - 
# mlflow.org////dvc.org is a tool
# normal projecct - 1 repository, 1 IDE
# AI - code repo, model Registry, data version control repo

# need a collaboration tool - 

# deployment compi
# tracking model should be present

# validation and testing techniques 

# excel sheet - metric of evaluation for all these tools
#     10 tools - 2 tools each






#model registry - example- image classification - 10 diff model_selection- track accuracy








