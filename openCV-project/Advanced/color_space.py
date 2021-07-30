import cv2
import matplotlib

import matplotlib.pyplot as plt
matplotlib.use('tkagg')

img = cv2.imread('Resources/Photos/cat.jpg')
# cv2.imshow('Images', img)

# Gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray', gray)

gray_to_bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
cv2.imshow('Gray to BGR', gray_to_bgr)

# HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
# cv2.imshow('HSV', hsv)

# LAMB
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
# cv2.imshow('LAB', lab)

# RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB', rgb)

plt.imshow(img)
plt.show()

cv2.waitKey(0)
