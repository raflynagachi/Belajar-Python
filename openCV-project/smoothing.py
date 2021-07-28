import cv2

img = cv2.imread('Resources/Photos/cats.jpg')

# Averaging
average = cv2.blur(img, (7, 7))
cv2.imshow('Average', average)

# Gaussian blur
gauss = cv2.GaussianBlur(img, (7, 7), 0)
cv2.imshow('Gaussian blur', gauss)

# Median blur
median = cv2.medianBlur(img, 7)
cv2.imshow('Median', median)

# Bilateral blur
bilateral = cv2.bilateralFilter(img, 20, 35, 25)
cv2.imshow('Bilateral', bilateral)

cv2.waitKey(0)
