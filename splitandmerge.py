import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")

blank = np.zeros(img.shape[:2], dtype="uint8")

b, g, r = cv.split(img)


blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])


cv.imshow("Blue", blue)
cv.imshow("green", green)
cv.imshow("red", red)

# cv.imshow("City", img)


cv.imshow("Blue", blue)
cv.imshow("Red", red)
cv.imshow("Green", green)

print(img.shape)
print(b.shape)
print(r.shape)
print(g.shape)

merge = cv.merge([b, g, r])

cv.imshow("Merged", merge)

cv.waitKey(0)
