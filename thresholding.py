import cv2 as cv

img = cv.imread("Photos/cats.jpg")

cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grey", gray)

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow("Thresh", thresh)

threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow("Thresh", thresh_inv)

adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                       cv.THRESH_BINARY, 11, 3)

cv.imshow("Adaptive Threshold", adaptive_thresh)


adaptive_thresh_inv = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                           cv.THRESH_BINARY_INV, 11, 3)

cv.imshow("Adaptive Threshold INV", adaptive_thresh_inv)
cv.waitKey(0)
