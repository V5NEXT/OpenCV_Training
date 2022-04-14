import cv2 as cv

img = cv.imread('Photos/cats.jpg')

cv.imshow("Cats", img)

grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grey", grey)

# Blurring the image
blur = cv.GaussianBlur(grey, (5, 5), cv.BORDER_DEFAULT)
cv.imshow("Blurring an Image", blur)

#edges or canny

canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Edges", canny)

# Finding the contours

contours, hierachies = cv.findContours(
    canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)

print(f'{len(contours)} contours in the image')
cv.waitKey(0)
