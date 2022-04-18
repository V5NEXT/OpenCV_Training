from cmath import rect
import cv2 as cv
from cv2 import bitwise_not
import numpy as np


blank = np.zeros((400, 400), dtype='uint8')
rectangle = cv.rectangle(blank.copy(), (30, 30), (350, 350), 255, -1)
circle = cv.circle(blank.copy(), (200, 200), 200, 255, -1)

cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)


bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("bitwise and", bitwise_and)

bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("bitwise Or", bitwise_or)

bitwise_no = cv.bitwise_not(rectangle, circle)
cv.imshow("bitwise not", bitwise_no)

# good for non intesection regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)


cv.imshow("bitwise xor", bitwise_xor)


cv.waitKey(0)
