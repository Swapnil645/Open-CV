import cv2 as cv
import numpy as np
import os

p=[]
DIR = os.getcwd() + '/Resources/Faces/train'
for i in os.listdir(DIR):
    p.append(i)
haar_cascade = cv.CascadeClassifier('haar_face.xml')

# features = np.load('features.npy')
# labels  = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yaml')

path = os.getcwd() + '/Resources/Faces/val/ben_afflek/2.jpg'
img = cv.imread(path)

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow('Person',gray)

#detect the face in imagez
faces_rect = haar_cascade.detectMultiScale(gray,1.1,4)

for (x,y,w,h) in faces_rect:
    faces_roi = gray[y:y+h,x:x+w]
    label,confidence = face_recognizer.predict(faces_roi)
    print(f'label = {p[label]} with a confidence of {confidence}')
    cv.putText(img,str(p[label]),(20,20),cv.FONT_HERSHEY_COMPLEX,1.0,(0,255,0),thickness=2)

    cv.rectangle(img,(x,y),(x+w,y+h),(0,255,0),thickness=2)

cv.imshow('Detected Face',img)

cv.waitKey(0)
