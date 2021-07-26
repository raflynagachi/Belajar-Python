import cv2
import numpy as np

img = cv2.imread('Resources/Photos/group 1.jpg')


def translate(img, x, y):
    # Translations
    # x-->Right, -x-->Left, y-->Down, -y-->Up
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])
    return cv2.warpAffine(img, transMat, dimensions)


def rotate(img, angle, rotPoint=None):
    # Rotations
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv2.warpAffine(img, rotMat, dimensions)


translated = translate(img, 100, -50)
rotated = rotate(img, -90)  # Minus to clockwise, Plus to anti-clockwise

# Resize
# Shrinking using default or INTER_AREA interpolataion
#  Enlarging using INTER_LINEAR (Faster) or
#   INTER_CUBIC (Slower but High Quality) interpolation
resized = cv2.resize(img, (500, 500), interpolation=cv2.INTER_AREA)

# Flipping
# 0 --> flip vertically
# 1 --> flip horizontally
# -1 --> flip vertically and horizontally
flipped = cv2.flip(img, 1)

# Cropping
cropped = img[200:, 50:]

cv2.imshow('Photos', rotated)

cv2.waitKey(0)
