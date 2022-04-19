import cv2 as cv
from cv2 import circle
import numpy as np

img = cv.imread("Photos/cats.jpg")


cv.imshow("Cats", img)
blank = np.zeros(img.shape[:2], dtype='uint8')


circle = cv.circle(
    blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)

rectangle = cv.rectangle(blank.copy(), (30, 30), (350, 350), 255, -1)

new_img = cv.bitwise_and(circle, rectangle)

masked = cv.bitwise_and(img, img, mask=new_img)

cv.imshow("Masked", masked)
cv.waitKey(0)
