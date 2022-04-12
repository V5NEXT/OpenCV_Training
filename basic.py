import cv2 as cv

img = cv.imread('Photos/park.jpg')

cv.imshow('Cat', img)

# Converting an image to gery scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

cv.imshow('Gray', gray)


# bluring an image

blur = cv.GaussianBlur(img, (3, 3), cv.BORDER_DEFAULT)

cv.imshow('Blur', blur)

# Edge Cascade

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny', canny)

# Dilating an image

dilated = cv.dilate(canny, (7, 7), iterations=3)
cv.imshow("dilated", dilated)

# eroding

erode = cv.erode(dilated, (7, 7), iterations=3)
cv.imshow("eroded", erode)

# resizing an image
resie = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("resize", resie)

# cropping
cropping = img[50:200, 200:500]
cv.imshow('cropped', cropping)
cv.waitKey(0)
