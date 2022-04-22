import numpy as np
import cv2 as cv

haar_cascade = cv.CascadeClassifier('haar_classifier.xml')


people = ['Ben Afflek', 'Elton John',
          'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
# features = np.load('features.npy')
# labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

img = cv.imread(
    r'C:\Users\vishn\OneDrive\Desktop\Science Crap\ML\OpenCV\Faces\val\jerry_seinfeld\2.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Person', gray)


# Detecting Faces
faces_rectangle = haar_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=2)


for(x, y, w, h) in faces_rectangle:
    faces_roi = gray[y:y+w, x:x+h]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f'label = {people[label]} with a confidence of {confidence}')

    cv.putText(img, str(people[label]), (20, 20), cv.FONT_HERSHEY_COMPLEX,
               1.0, (0, 255, 0), thickness=2)
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)

cv.imshow("Detected Image", img)


cv.waitKey(0)
