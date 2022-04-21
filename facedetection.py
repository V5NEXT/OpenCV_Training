import cv2 as cv


img = cv.imread("Photos/group 1.jpg")

cv.imshow("Lady", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow("Gray Lady", gray)

haar_cascade = cv.CascadeClassifier('haar_classifier.xml')

faces_rectangle = haar_cascade.detectMultiScale(
    gray, scaleFactor=1.1, minNeighbors=2)

print(f'Number of faces = {len(faces_rectangle)}')

for(x, y, w, h) in faces_rectangle:
    cv.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), thickness=2)


cv.imshow("Face Detected", img)
cv.waitKey(0)
