import cv2 as cv
import numpy as np

# Read images
# img = cv.imread('Resources/Photos/cat_large.jpg')
# cv.imshow('cat', np.array(img, dtype=np.uint8))
# cv.waitKey()

# Read videos (Webcam/videos file)
capture = cv.VideoCapture(0)
webcam = capture.isOpened()

while webcam:
    isTrue, frame = capture.read()

    if isTrue:
        # Add grayscale filter
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Fliping the image as said in question
        gray_flip = cv.flip(gray, 1)
        frame_flip = cv.flip(frame, 1)

        # Combining the two different image frames in one window
        combined_window = np.hstack([gray, gray_flip])

        cv.imshow('video', frame_flip)

    if cv.waitKey(1) == ord('q'):
        break

capture.release()
cv.destroyAllWindows()
