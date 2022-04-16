import cv2 as cv

img = cv.imread("Photos/cats.jpg")


cv.imshow("Cats", img)

# Averegaing Blur

average = cv.blur(img, (3, 3))
cv.imshow("Average Blur", average)


# Guassian Blur

guass = cv.GaussianBlur(img, (3, 3), 0)
cv.imshow("Guassian Blur", guass)

# Median Blur
median = cv.medianBlur(img, 3)
cv.imshow("Median", median)

# Bilateral Blur
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow("Bilateral", bilateral)


cv.waitKey(0)
