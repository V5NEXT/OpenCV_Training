import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')

cv.imshow("Cats", img)

# createing a blank image
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow("Blank Image", blank)

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grey", grey)

# Blurring the image
blur = cv.GaussianBlur(grey, (5, 5), cv.BORDER_DEFAULT)
cv.imshow("Blurring an Image", blur)

#edges or canny

canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Edges", canny)

# USing Threshold
# ret, thresh = cv.threshold(grey, 125, 255, cv.THRESH_BINARY)
# cv.imshow("Threshold Image", thresh)
# Finding the contours

contours, hierachies = cv.findContours(
    canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

print(f'{len(contours)} contours in the image')

cv.drawContours(blank, contours, -1, (0, 0, 255), 2)
cv.imshow("COntour Drawn Blank Image", blank)

cv.waitKey(0)
