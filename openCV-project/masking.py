import cv2
import numpy as np

img = cv2.imread('Resources/Photos/cats.jpg')
blank = np.zeros(img.shape[:2], dtype='uint8')
circle = cv2.circle(
    blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
rectangle = cv2.rectangle(blank.copy(), (150, 150), (400, 400), 255, -1)
mask = cv2.bitwise_and(circle, rectangle)
masked = cv2.bitwise_and(img, img, mask=mask)

cv2.imshow('Images', masked)

cv2.waitKey(0)
