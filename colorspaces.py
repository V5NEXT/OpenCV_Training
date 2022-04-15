import cv2 as cv

img = cv.imread("Photos/lady.jpg")

cv.imshow("City", img)

# BGE to Grey Scale

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray Scale", grey)

# BGR to HSV

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow("HSV", hsv)

# BGR to LAB

lab = cv.cvtColor(img, cv.COLOR_RGB2Lab)
cv.imshow("LAB", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("RGB", rgb)

cv.waitKey(0)
