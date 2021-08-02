import cv2
import numpy as np

cam = cv2.VideoCapture(0)

myColors = [[5, 107, 0, 19, 255, 255],
            [133, 56, 0, 159, 156, 255]]

myColorValue = [[51, 153, 255],  # BGR
                [255, 0, 255]]

myPoints = []  # [x, y, colorID]


def findColor(img, myColor, myColorValue):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    newPoints = []
    for index, color in enumerate(myColor):
        lower = np.array(color[:3])
        upper = np.array(color[3:])
        mask = cv2.inRange(imgHSV, lower, upper)
        x, y = getContours(mask)
        cv2.circle(imgResult, (x, y), 10, myColorValue[index], -1)
        # cv2.imshow(str(color), mask)

        if x != 0 and y != 0:
            newPoints.append([x, y, index])

    return newPoints


def getContours(img):
    x, y, w, h = 0, 0, 0, 0
    contours, hierarchy = cv2.findContours(
        img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:
            # cv2.drawContours(imgResult, cnt, -1, (255, 0, 0), 3)
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.02*peri, True)
            x, y, w, h = cv2.boundingRect(approx)
    return x+w//2, y


def drawOnCanvas(myPoint, myColorValue):
    for point in myPoint:
        cv2.circle(imgResult, (point[0], point[1]),
                   10, myColorValue[point[2]], -1)


while True:
    isTrue, img = cam.read()
    img = cv2.flip(img, 1)
    imgResult = img.copy()

    newPoints = findColor(img, myColors, myColorValue)

    if len(newPoints) != 0:
        for newP in newPoints:
            myPoints.append(newP)

    if len(myPoints) != 0:
        drawOnCanvas(myPoints, myColorValue)

    cv2.imshow('Paint Virtual', imgResult)

    if cv2.waitKey(1) == ord('q'):
        break
