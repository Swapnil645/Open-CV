import cv2 as cv
import mediapipe as mp
import time

cap = cv.VideoCapture('Resources/4.mp4')
ptime = 0
mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2,min_detection_confidence=0.10,min_tracking_confidence=0.30)
drawSpec = mpDraw.DrawingSpec(thickness=1,circle_radius=2)
while True:

    success,img = cap.read()
    imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)

    if results.multi_face_landmarks:
        for facelm in results.multi_face_landmarks:
            mpDraw.draw_landmarks(img,facelm,mpFaceMesh.FACEMESH_TESSELATION,drawSpec,drawSpec)

            for lm in facelm.landmark:
                h,w,c = img.shape
                cx,cy = int(lm.x*w),int(lm.y*h)
                print(cx,cy)

                

    ctime= time.time()
    fps = 1/(ctime-ptime)
    ptime =ctime
    cv.putText(img,str(int(fps)),(20,70),cv.FONT_HERSHEY_COMPLEX,3,(0,255,0),2)
    cv.imshow('image',img)
    cv.waitKey(2)