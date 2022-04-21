from pyexpat import features
import cv2 as cv
import os
import numpy as np


people = []
DIR = r'C:\Users\vishn\OneDrive\Desktop\Science Crap\ML\OpenCV\Faces\train'
haar_cascade = cv.CascadeClassifier('haar_classifier.xml')

for i in os.listdir(r'C:\Users\vishn\OneDrive\Desktop\Science Crap\ML\OpenCV\Faces\train'):
    people.append(i)
features = []
labels = []


def createtrain():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            face_detect = haar_cascade.detectMultiScale(
                gray, scaleFactor=1.1, minNeighbors=4)

            for(x, y, w, h) in face_detect:
                faceofintrest = gray[y:y+h, x:x+w]
                features.append(faceofintrest)
                labels.append(label)


createtrain()
