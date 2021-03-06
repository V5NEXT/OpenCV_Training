from turtle import width
import cv2 as cv
import numpy as np

img = cv.imread('Photos/park.jpg')

cv.imshow("Park", img)

# translating an image


def translate(img, x, y):
    transMatrix = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMatrix, dimensions)


translated = translate(img, 100, 200)
cv.imshow("Translated Image", translated)


# rotate an image

def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, 25)
cv.imshow("Rotated", rotated)


# resizing the image

resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow("Resized", resized)

# flipping Images  0= vertical, 1 = horizontal, -1 = both
flip = cv.flip(img, 0)
cv.imshow("Flipped ", flip)

cv.waitKey(0)
