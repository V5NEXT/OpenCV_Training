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


cv.waitKey(0)
