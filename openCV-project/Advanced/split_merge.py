import cv2
import numpy as np

img = cv2.imread('Resources/Photos/cat.jpg')
# cv2.imshow('Images', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

b, g, r = cv2.split(img)

# Color channel
blue = cv2.merge([b, blank, blank])
green = cv2.merge([blank, g, blank])
red = cv2.merge([blank, blank, r])

# Grayscale channel
cv2.imshow('Blue', b)
cv2.imshow('Green', g)
cv2.imshow('Red', r)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Merge image
merge = cv2.merge([b, g, r])
cv2.imshow('Merge', merge)

cv2.waitKey(0)
