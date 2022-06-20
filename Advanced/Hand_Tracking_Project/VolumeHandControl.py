import cv2 as cv
import time
import numpy as np
import HandTrackingModule as htm
import math

from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume



wCam, hCam = 1280,720

cap = cv.VideoCapture(0)
handDetector = htm.handDetector(detectionCon=0.7)
cap.set(3,wCam)
cap.set(4,hCam)
ptime=0

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
#volume.GetMute()
volume.GetMasterVolumeLevel()
volumeRange = volume.GetVolumeRange()
volume.SetMasterVolumeLevel(0.0, None)

minVol = volumeRange[0]
maxVol = volumeRange[1]





vol=0
while True:
    success,img = cap.read()
    img = handDetector.findHands(img)
    lmlist= handDetector.findPosition(img,draw=False)
    
    if len(lmlist):

        x1,y1 = lmlist[4][1],lmlist[4][2]
        x2,y2 = lmlist[8][1],lmlist[8][2]
        cx,cy = (x1+x2)//2, (y1+y2)//2

        cv.circle(img,(x1,y1),15,(255,0,255),cv.FILLED)
        cv.circle(img,(x2,y2),15,(255,0,255),cv.FILLED)
        cv.line(img,(x1,y1),(x2,y2),(255,0,255),2)
        cv.circle(img,(cx,cy),15,(255,0,255),cv.FILLED)

        length=math.hypot(x2-x1,y2-y1)
        print(length)

        if length<50:
            cv.circle(img,(cx,cy),15,(0,255,0),cv.FILLED)

        #hand Range 50 to 300
        #Volume Range -65 to 0

        vol = np.interp(length,[50,300],[minVol,maxVol])
        
        volume.setMasterVolumeLevel(vol,None)
    
    cv.rectangle(img,(50,150),(85,400),(0,255,0),3)
    cv.rectangle(img,(50,int(vol)),(85,400),(0,255,0),cv.FILLED)

    ctime =time.time()
    fps=1/(ctime-ptime)
    ptime=ctime
    cv.putText(img,str(int(fps)),(20,50),cv.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)
    cv.imshow('imgae',img)
    cv.waitKey(1)
