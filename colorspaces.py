import cv2 as cv

img = cv.imread("Photos/park.jpg")

cv.imshow("City", img)

cv.waitKey(0)
