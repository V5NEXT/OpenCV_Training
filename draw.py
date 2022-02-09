from signal import valid_signals
import cv2 as cv
import numpy as np


# create a blank image
blank = np.zeros((500, 500, 3), dtype="uint8")

# Painting image with a color
#blank[:] = 0, 255, 0


# paint certain area

# blank[200:300, 300:400] = 0, 0, 255

# drawing a rectangle
# to fill sliced part we give thickeness = Filled
cv.rectangle(blank, (0, 0), (250, 250), (0, 255, 0), thickness=2)


# draw circle

cv.circle(blank, (blank.shape[1]//2,
          blank.shape[0]//2), 40, (0, 0, 255), thickness=3)
# draw a line


cv.line(blank, (0, 0), (blank.shape[1]//2,
        blank.shape[0]//2), (255, 255, 255), thickness=3)

# writing a text

cv.putText(blank, 'sample text', (225, 225),
           cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), 2)

cv.imshow('portion', blank)


cv.waitKey(0)
