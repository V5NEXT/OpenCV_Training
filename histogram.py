import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread("Photos/cats.jpg")


cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

# created grayscale histograms
gray_histogram = cv.calcHist([gray], [0], None, [256], [0, 256])
plt.figure()
plt.title("Gray Scale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(gray_histogram)
plt.xlim([0, 256])
plt.show()

cv.waitKey(0)
