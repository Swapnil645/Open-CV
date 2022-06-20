from cProfile import label
from tkinter import E
import cv2
import os
import cv2 as cv
import numpy as np

p = []
DIR = os.getcwd() + '/Resources/Faces/train'
for i in os.listdir(DIR):
    p.append(i)

haar_cascade = cv.CascadeClassifier('haar_face.xml')
features = []
labels = []

def create_train():
    #path = os.getcwd() + '/Resources/Faces/train'
    for person in p:
        path = os.path.join(DIR,person)
        label = p.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path,img)
            img_array = cv.imread(img_path)

            gray = cv.cvtColor(img_array,cv.COLOR_BGR2GRAY)
            faces_rect = haar_cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray[y:y+h,x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()

print('features', len(features))
print('labels',len(labels))
print('Training done')
features = np.array(features,dtype=object)
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()
#Train the recognizer on the features list and labels list

face_recognizer.train(features,labels)
face_recognizer.save('face_trained.yaml')
np.save('features.npy',features)
np.save('labels.npy',labels)
print(p)



