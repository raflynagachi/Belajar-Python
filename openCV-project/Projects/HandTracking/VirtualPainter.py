import cv2
import numpy as np
import time
import os
import hand_tracking_module as htm

#######################
wCam, hCam = 1080, 640
brushThickness = 10
#######################

folderPath = 'Projects/HandTracking/Resources'
myList = os.listdir(folderPath)
overlayList = []
for imgPath in myList:
    image = cv2.imread(f'{folderPath}/{imgPath}')
    image = cv2.resize(image, (640, 90),
                       interpolation=cv2.INTER_AREA)
    overlayList.append(image)
header = overlayList[3]
drawColor = (255, 0, 0)
print(myList)

cap = cv2.VideoCapture(0)
hCam, wCam = cap.read()[1].shape[:-1]
detector = htm.handDetector(detectionCon=0.85)
pTime = 0

xp, yp = 0, 0
imgCanvas = np.zeros((hCam, wCam, 3), np.uint8)

while True:
    # 1. import image
    success, img = cap.read()

    # 2. find landmarks
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        # print(lmList)

        # Tip of index and middle fingers
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]

        # 3. Which finger are up
        fingers = detector.fingersUp()
        # print(fingers)

        if fingers[1] and fingers[2]:
            cv2.rectangle(img, (x1, y1-25), (x2, y2+25),
                          drawColor, cv2.FILLED)
            # print('Selection mode')
            # Checking for the brush
            xp, yp = 0, 0
            if y1 < 100:
                if 140 < x1 < 220:
                    header = overlayList[3]
                    drawColor = (255, 0, 255)
                elif 280 < x1 < 360:
                    header = overlayList[0]
                    drawColor = (255, 0, 0)
                elif 420 < x1 < 490:
                    header = overlayList[2]
                    drawColor = (0, 255, 0)
                elif 540 < x1 < 610:
                    header = overlayList[1]
                    drawColor = (0, 0, 0)

        if not (fingers[1] and fingers[2]):
            cv2.circle(img, (x1, y1), 10, drawColor, cv2.FILLED)
            # print('Drawing mode')
            if xp == 0 and yp == 0:
                xp, yp = x1, y1

            if drawColor == (0, 0, 0):
                brushThickness = 50
            else:
                brushThickness = 10

            cv2.line(img, (xp, yp), (x1, y1), drawColor, brushThickness)
            cv2.line(imgCanvas, (xp, yp), (x1, y1), drawColor, brushThickness)
            xp, yp = x1, y1

    imgGray = cv2.cvtColor(imgCanvas, cv2.COLOR_BGR2GRAY)
    _, imgInv = cv2.threshold(imgGray, 20, 255, cv2.THRESH_BINARY_INV)
    imgInv = cv2.cvtColor(imgInv, cv2.COLOR_GRAY2BGR)
    img = cv2.bitwise_and(img, imgInv)
    img = cv2.bitwise_or(img, imgCanvas)

    # Settings header image
    img[:90, :640] = header

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 450),
                cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    # img = cv2.addWeighted(img, 0.5, imgCanvas, 0.5, 0)

    cv2.imshow('Images', img)
    # cv2.imshow('Drawing', imgGray)
    # cv2.imshow('Drawing1', imgInv)

    if cv2.waitKey(1) == ord('q'):
        break
