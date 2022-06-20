import cv2 as cv

import mediapipe as mp
import time

cap = cv.VideoCapture('Resources/6.mp4')
mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()
ptime = 0

def rescaleFrame(frame,scale=.45):
    #works for everything
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimension = (width,height)
    return cv.resize(frame,dimension, interpolation=cv.INTER_AREA)


while True:
    success,img = cap.read()
    img = rescaleFrame(img)
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    if results.detections:
        for id,detection in enumerate(results.detections):
            print(id,detection.location_data.relative_bounding_box)
            mpDraw.draw_detection(img,detection)
            bboxC = detection.location_data.relative_bounding_box
            ih,iw,ic = img.shape
            bbox = int(bboxC.xmin*iw),int(bboxC.ymin*ih),int(bboxC.width*iw),int(bboxC.height*ih)
            cv.rectangle(img,bbox,(255,0,255),2)
            cv.putText(img,str(int(detection.score[0]*100)),(bbox[0],bbox[1]-20),cv.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)

    ctime =time.time()
    fps = 1/(ctime-ptime)
    ptime =ctime

    cv.putText(img,str(int(fps)),(20,70),cv.FONT_HERSHEY_COMPLEX,3,(255,0,0),2)
    cv.imshow('image',img)

    cv.waitKey(1)