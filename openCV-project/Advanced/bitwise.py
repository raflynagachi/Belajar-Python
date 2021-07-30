import cv2
import numpy as np

blank = np.zeros((400, 400), dtype='uint8')

circle = cv2.circle(blank.copy(), (200, 200), 200, 255, -1)
rectangle = cv2.rectangle(blank.copy(), (20, 20), (380, 380), 255, -1)

# cv2.imshow('Circle', circle)
# cv2.imshow('Rectangle', rectangle)

# bitwise AND
bitwise_and = cv2.bitwise_and(circle, rectangle)
cv2.imshow('Bitwise AND', bitwise_and)

# bitwise OR
bitwise_or = cv2.bitwise_or(circle, rectangle)
cv2.imshow('Bitwise OR', bitwise_or)

# bitwise XOR
bitwise_xor = cv2.bitwise_xor(circle, rectangle)
cv2.imshow('Bitwise XOR', bitwise_xor)

# bitwise NOT
bitwise_not = cv2.bitwise_not(circle, rectangle)
cv2.imshow('Bitwise NOT', bitwise_not)

cv2.waitKey(0)
