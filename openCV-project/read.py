import cv2
import numpy as np

# Read images
# img = cv2.imread('Resources/Photos/cat_large.jpg')
# cv2.imshow('cat', np.array(img, dtype=np.uint8))
# cv2.waitKey()

# Read videos (Webcam/videos file)
capture = cv2.VideoCapture(0)
webcam = capture.isOpened()

while webcam:
    isTrue, frame = capture.read()

    if isTrue:
        # Add grayscale filter
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Fliping the image as said in question
        gray_flip = cv2.flip(gray, 1)
        frame_flip = cv2.flip(frame, 1)

        # Combining the two different image frames in one window
        combined_window = np.hstack([gray, gray_flip])

        cv2.imshow('video', frame_flip)

    if cv2.waitKey(1) == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()
