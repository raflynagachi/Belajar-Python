import cv2


def rescaleFrame(frame, scale=.75):
    # work for images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)


img = cv2.imread('Resources/Photos/cat.jpg')
# cv2.imshow('Photos', img)
img = rescaleFrame(img, 0.75)

# Gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Gray', gray)

# Blur
blur = cv2.GaussianBlur(img, (3, 3), cv2.BORDER_DEFAULT)
# cv2.imshow('Blur', blur)

# Edge cascade
edge = cv2.Canny(blur, 125, 175)
# cv2.imshow('Edge cascade', edge)

# Dilating the image
dilated = cv2.dilate(edge, (7, 7), iterations=3)
# cv2.imshow('Dilated', dilated)

# Eroding
eroded = cv2.erode(dilated, (7, 7), iterations=3)
# cv2.imshow('Erode', eroded)

# Resize
resized = cv2.resize(img, (1200, 600), interpolation=cv2.INTER_LINEAR)
# cv2.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 100:200]
cv2.imshow('Cropped', cropped)

cv2.waitKey(0)
