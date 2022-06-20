import cv2 as cv

import mediapipe as mp
import time

def rescaleFrame(frame,scale=.45):
        #works for everything
        width = int(frame.shape[1]*scale)
        height = int(frame.shape[0]*scale)

        dimension = (width,height)
        return cv.resize(frame,dimension, interpolation=cv.INTER_AREA)

class FaceDetector():

    def __init__(self,minDetectionCon=0.5):
        self.minDetectionCon = minDetectionCon
        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(self.minDetectionCon)


    
    def findFaces(self,img,draw=True):
        img = rescaleFrame(img)
        imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB)
        bboxlist = []
        if self.results.detections:
            for id,detection in enumerate(self.results.detections):
                #print(id,detection.location_data.relative_bounding_box)
                self.mpDraw.draw_detection(img,detection)
                bboxC = detection.location_data.relative_bounding_box
                ih,iw,ic = img.shape
                bbox = int(bboxC.xmin*iw),int(bboxC.ymin*ih),int(bboxC.width*iw),int(bboxC.height*ih)
                bboxlist.append([id,bbox,detection.score])
                
                img = self.fancyDraw(img,bbox)
                cv.putText(img,str(int(detection.score[0]*100)),(bbox[0],bbox[1]-20),cv.FONT_HERSHEY_COMPLEX,1,(255,0,0),2)

        return img,bboxlist

    def fancyDraw(self,img,bbox,l=38,t=7):
        x,y,w,h = bbox
        x1,y1 = x+w,y+h
       
        cv.rectangle(img,bbox,(255,0,255),1)
        #top left
        cv.line(img,(x,y),(x+l,y),(255,0,255),t)
        cv.line(img,(x,y),(x,y+l),(255,0,255),t)

        #top right
        cv.line(img,(x1,y),(x1-l,y),(255,0,255),t)
        cv.line(img,(x1,y),(x1,y+l),(255,0,255),t)


        #bottom left
        cv.line(img,(x,y1),(x+l,y1),(255,0,255),t)
        cv.line(img,(x,y1),(x,y1-l),(255,0,255),t)

        #bottom right
        cv.line(img,(x1,y1),(x1-l,y1),(255,0,255),t)
        cv.line(img,(x1,y1),(x1,y1-l),(255,0,255),t)
        return img
                        
                    
       

def main():
    cap = cv.VideoCapture('Resources/1.mp4')
    ptime = 0
    detector = FaceDetector()
    while True:
        success,img = cap.read()
       
        img,bbox = detector.findFaces(img)
        print(bbox)
        ctime =time.time()
        fps = 1/(ctime-ptime)
        ptime =ctime

        cv.putText(img,str(int(fps)),(20,70),cv.FONT_HERSHEY_COMPLEX,3,(255,0,0),2)
        cv.imshow('image',img)

        cv.waitKey(1)


if __name__ == "__main__":
    main()