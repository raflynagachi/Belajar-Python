import cv2
import numpy as np

img = cv2.imread('Resources/Photos/park.jpg')
# cv2.imshow('Images', img)

blank = np.zeros(img.shape, dtype='uint8')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
canny = cv2.Canny(blur, 125, 175)

# Option 1: findContours
# RETR_TREE --> All hierarchical contours
# RETR_LIST --> All contours in the image
# RETR_EXTERNAL --> Only external contours
contour, hierarchies = cv2.findContours(
    canny, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
print('{} contours found!'.format(len(contour)))

cv2.drawContours(blank, contour, -1, (0, 255, 0), 1)
cv2.imshow('Blank', blank)

# Option 2: Threshold
# If <125 change to white, if >255 change to black
ret, thresh = cv2.threshold(canny, 125, 255, type=cv2.THRESH_BINARY)
cv2.imshow('Thresh', thresh)

cv2.waitKey(0)
