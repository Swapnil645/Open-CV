import cv2 as cv
import mediapipe as mp
import time

def rescaleFrame(frame,scale=.40):
    #works for everything
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimension = (width,height)
    return cv.resize(frame,dimension, interpolation=cv.INTER_AREA)

cap =  cv.VideoCapture('Resources/1.mp4')

mpPose = mp.solutions.pose
pose = mpPose.Pose()
mpDraw = mp.solutions.drawing_utils


ptime=0
while True:
    success,img = cap.read()
    resized_img = rescaleFrame(img)
    imgRGB = cv.cvtColor(resized_img,cv.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(resized_img,results.pose_landmarks,mpPose.POSE_CONNECTIONS)
        for id,lm in enumerate(results.pose_landmarks.landmark):
            h,w,c = resized_img.shape
            print(id,lm)
            cx,cy = int(lm.x * w),int(lm.y*h)

            cv.circle(resized_img,(cx,cy),10,(255,0,255),cv.FILLED)



    ctime = time.time()
    fps = 1/(ctime-ptime)
    ptime = ctime
    cv.putText(resized_img,str(int(fps)),(70,50),cv.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)
    cv.imshow('image',resized_img)

    cv.waitKey(1)