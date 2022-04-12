import cv2 as cv

img = cv.imread('Photos/cat.jpg')

cv.imshow('Cat', img)

# Converting an image to gery scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Gray', gray)


# bluring an image

cv.waitKey(0)
