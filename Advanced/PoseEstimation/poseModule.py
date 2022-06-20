import cv2 as cv
import mediapipe as mp
import time,math

def rescaleFrame(frame,scale=.40):
    #works for everything
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)

    dimension = (width,height)
    return cv.resize(frame,dimension, interpolation=cv.INTER_AREA)

class poseDetector():
    def __init__(self,mode=False,complexity=1,upperbody=False,smooth=True,detectioncon=0.5,trackcon=0.5):
        self.mode = mode
        self.upperbody = upperbody
        self.smooth= smooth
        self.detectioncon=detectioncon
        self.trackcon=trackcon

        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(self.mode,complexity,self.upperbody,self.smooth,self.detectioncon,self.trackcon)
        self.mpDraw = mp.solutions.drawing_utils


    def findPose(self,resized_img,draw = True):
        #resized_img = rescaleFrame(img)
        imgRGB = cv.cvtColor(resized_img,cv.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)

        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(resized_img,self.results.pose_landmarks,self.mpPose.POSE_CONNECTIONS)
            

        return resized_img


    def findPosition(self,img,draw = True):
        self.lmlist=[]
        if self.results.pose_landmarks:
            for id,lm in enumerate(self.results.pose_landmarks.landmark):
                h,w,c = img.shape
                cx,cy = int(lm.x * w),int(lm.y*h)
                self.lmlist.append([id,cx,cy])
                if draw:
                    cv.circle(img,(cx,cy),3,(255,255,),cv.FILLED)

        return self.lmlist   

    def findAngle(self,img,p1,p2,p3,draw=True):
        #Get the landmarks
        x1,y1 = self.lmlist[p1][1:]
        x2,y2 = self.lmlist[p2][1:]
        x3,y3 = self.lmlist[p3][1:]

        #get angle
        angle = math.degrees(math.atan2(y3-y2,x3-x2)- math.atan2(y1-y2,x1-x2))
        if angle<0:
            angle +=360
        
        if draw:
            cv.line(img,(x1,y1),(x2,y2),(255,255,255),3)
            cv.line(img,(x3,y3),(x3,y3),(255,255,255),3)
            cv.circle(img,(x1,y1),10,(0,255,0),cv.FILLED)
            cv.circle(img,(x1,y1),15,(0,0,255),2)
            cv.circle(img,(x2,y2),10,(0,255,0),cv.FILLED)
            cv.circle(img,(x2,y2),15,(0,0,255),2)
            cv.circle(img,(x3,y3),10,(0,255,0),cv.FILLED)
            cv.circle(img,(x3,y3),15,(0,0,255),2)
            cv.putText(img,str(int(angle)),(x2-50,y2+50),cv.FONT_HERSHEY_COMPLEX,2,(255,0,255),2)

        return angle,img
   

def main():
    cap =  cv.VideoCapture('Resources/1.mp4')

    ptime=0
    detector = poseDetector()
    while True:
        success,img = cap.read()
        resized_img = detector.findPose(img)
        lmlist = detector.findPosition(resized_img)

        if len(lmlist):
            img = detector.findAngle(img,12,14,16)
        ctime = time.time()
        fps = 1/(ctime-ptime)
        ptime = ctime
        cv.putText(resized_img,str(int(fps)),(70,50),cv.FONT_HERSHEY_COMPLEX,3,(255,0,0),3)
        cv.imshow('image',resized_img)
        cv.waitKey(1)





if __name__ == "__main__":
    main()
