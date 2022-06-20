import cv2 as cv
import mediapipe as mp
import time

class faceMeshDetector():
    def __init__(self,mode=False,max_faces=2, minDetectionCon=0.5,minTrackingCon=0.5):
        self.mode = mode
        self.max_num_faces=max_faces
        self.minDetectionCon=minDetectionCon
        self.minTrackingCon=minTrackingCon



        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(max_num_faces=self.max_num_faces,min_detection_confidence=self.minDetectionCon,min_tracking_confidence=self.minTrackingCon)
        self.drawSpec = self.mpDraw.DrawingSpec(thickness=1,circle_radius=2)

    def findFaceMesh(self,img,draw=True):
        imgRGB = cv.cvtColor(img,cv.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(imgRGB)
        faces=[]
        if self.results.multi_face_landmarks:
            for facelm in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img,facelm,self.mpFaceMesh.FACEMESH_TESSELATION,self.drawSpec,self.drawSpec)
       
                face=[]
                for id,lm in enumerate(facelm.landmark):
                    h,w,c = img.shape
                    cx,cy = int(lm.x*w),int(lm.y*h)
                    cv.putText(img,str(int(id)),(cx,cy),cv.FONT_HERSHEY_COMPLEX,0.5,(0,255,0),1)
                    face.append([id,cx,cy])
                faces.append(face)
        return img,faces   


def main():
    cap = cv.VideoCapture('Resources/4.mp4')
    ptime = 0
    detector = faceMeshDetector()
    while True:

        success,img = cap.read()
        img,faces = detector.findFaceMesh(img)
        if len(faces):
            print(faces)
        ctime= time.time()
        fps = 1/(ctime-ptime)
        ptime =ctime
        cv.putText(img,str(int(fps)),(20,70),cv.FONT_HERSHEY_COMPLEX,3,(0,255,0),2)
        cv.imshow('image',img)
        cv.waitKey(2)


if __name__ == "__main__":
    main()