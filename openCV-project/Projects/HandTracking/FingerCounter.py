import cv2
import time
# import os
import hand_tracking_module as htm

#############################
wCam, hCam = 680, 480
#############################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

# folderPath = 'FingerImages'
# myList = os.listdir(folderPath)
# print(myList)
# overlayList = []
# for path in myList:
#     image = cv2.imread(f'{folderPath}/{path}')
#     overlayList.append(image)

pTime = 0
# h, w, c = overlayList[0].shape

detector = htm.handDetector(detectionCon=0.75)
tipIds = [4, 8, 12, 16, 20]

while True:
    success, img = cap.read()

    # img[:w, :h] = overlayList[0]
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False)
    # print(lmList)

    if len(lmList) != 0:
        fingers = []

        # Thumbs
        if lmList[tipIds[0]][1] < lmList[tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4 fingers
        for id in tipIds[1:]:
            if lmList[id][2] < lmList[id-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        # Total fingers
        total = fingers.count(1)
        # print(total)

        cv2.putText(img, str(total), (20, 70),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 255), 2)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (400, 70),
                cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)
    cv2.imshow('Images', img)

    if cv2.waitKey(1) == ord('q'):
        break
