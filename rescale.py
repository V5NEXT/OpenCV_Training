import cv2 as cv


# reading Images
# img = cv.imread('Photos/cat.jpg')

# cv.imshow('Cat', img)


# Resizing frame


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# Changing resolution for live videos


def changeRes(width, height):
    capture.set(3, width)
    capture.set(4, height)

# reading videos


capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame)
    cv.imshow('Video', frame)
    cv.imshow('Video Rescaled', frame_resized)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

capture.release()
cv.destroyAllWindows()
