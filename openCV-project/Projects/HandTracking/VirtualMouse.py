import cv2
import numpy as np
import hand_tracking_module as htm
import time
import pyautogui

##########################################
cap = cv2.VideoCapture(0)
hCam, wCam = cap.read()[1].shape[:2]
wScreen, hScreen = pyautogui.size()
frameR = 100
smoothening = 10
##########################################
print(wCam, hCam)
print(wScreen, hScreen)

pTime = 0
pLocX, pLocY = 0, 0
cLocX, cLocY = 0, 0

detector = htm.handDetector(maxHands=1, detectionCon=0.80)

while True:
    # 1. Find hand landmark
    success, img = cap.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)

    cv2.rectangle(img, (frameR, frameR),
                  (wCam-frameR, hCam-frameR), (0, 255, 0), 2)

    # 2. Get the tip of the index and middle fingers
    if len(lmList) != 0:
        x1, y1 = lmList[8][1:]
        x2, y2 = lmList[12][1:]
        # print(x1, y1, x2, y2)

        # 3. Check which finger are up
        fingers = detector.fingersUp()
        print(fingers)

        # 4. Only index finger: Moving mode
        if fingers[1] == 1 and fingers[2] == 0:
            # 5. Convert coordinates
            x3 = np.interp(x1, (frameR, wCam-frameR), (0, wScreen))
            y3 = np.interp(y1, (frameR, hCam-frameR), (0, hScreen))

            # 6. Smoothen values
            cLocX = pLocX + (x3-pLocX) / smoothening
            cLocY = pLocY + (y3-pLocY) / smoothening

            # 7. Move mouse
            cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
            pyautogui.moveTo(cLocX, cLocY)

            pLocX, pLocY = cLocX, cLocY

        # 8. Both index and middle fingers are up: Clicking mode
        elif fingers[1] == 1 and fingers[2] == 1:
            # 9. Find distance between fingers
            length, img, lineInfo = detector.findDistance(8, 12, img)

            # 10. Click mouse if distance short
            if length < 40:
                cv2.circle(img, (lineInfo[4], lineInfo[5]),
                           15, (0, 255, 0), cv2.FILLED)
                pyautogui.click()

    # 11. Frame rate
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 50),
                cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    # 12. Display
    cv2.imshow('Images', img)
    if cv2.waitKey(1) == ord('q'):
        break
