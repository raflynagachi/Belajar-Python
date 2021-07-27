import cv2
import numpy as np

# blank image with 500x500 dimension and 3 layer channel (RGB)
blank = np.zeros((500, 500, 3), dtype='uint8')
# cv2.imshow('Blank', blank)

# Paint the image (Blue, Green, Red)
blank[100:200, 250:] = 105, 50, 100

cv2.rectangle(
    blank, (0, 0), (blank.shape[1]//2, blank.shape[0]//2),
    (255, 0, 0), thickness=-1)
cv2.circle(
    blank, (blank.shape[1]//2, blank.shape[0]//2),
    40, (0, 0, 255), thickness=-1)
cv2.line(blank, (200, 150),
         (blank.shape[1]//4, blank.shape[0]//2), (255, 255, 0), thickness=5)
cv2.putText(blank, 'Hello, Nagachi!', (100, 400),
            cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 50, 140), 2)

cv2.imshow('Images', blank)

cv2.waitKey(0)
