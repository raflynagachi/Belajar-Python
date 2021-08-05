import cv2
import hand_tracking_module as htm
import time
import numpy as np
import math
# from ctypes import cast, POINTER
# from comtypes import CLSCTX_ALL
# from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import subprocess
from subprocess import call

# Ubuntu environment
#############################
wCam, hCam = 680, 480
#############################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)

detector = htm.handDetector(detectionCon=0.7)
pTime = 0
volume = 50
call(["amixer", "-D", "pulse", "sset", "Master",
     str(volume)+"%"], stdout=subprocess.PIPE)

# # For windows OS
# devices = AudioUtilities.GetSpeakers()
# interface = devices.Activate(
#     IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
# volume = cast(interface, POINTER(IAudioEndpointVolume))
# # volume.GetMute()
# # volume.GetMasterVolumeLevel()
# volRange = volume.GetVolumeRange()
# minVol = volRange[0]
# maxVol = volRange[1]

while True:
    succes, img = cap.read()
    img = detector.findHands(img, draw=True)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        # print(lmList[4], lmList[8])
        x1, y1 = lmList[4][1], lmList[4][2]
        x2, y2 = lmList[8][1], lmList[8][2]

        x3, y3 = lmList[9][1], lmList[9][2]
        x4, y4 = lmList[12][1], lmList[12][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2

        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.circle(img, (x1, y1), 10, (255, 0, 0), -1)
        cv2.circle(img, (x2, y2), 10, (255, 0, 0), -1)
        cv2.circle(img, (cx, cy), 10, (255, 0, 0), -1)

        length = math.hypot(x2-x1, y2-y1)
        # print(length)

        if length < 40:
            cv2.circle(img, (cx, cy), 10, (0, 0, 255), -1)

        # For windows OS
        # volume = np.interp(length, [50, 300], [minVol, maxVol])
        # print(int(length), volume)
        # volume.SetMasterVolumeLevel(volume, None)
        if y4 > y3:
            cv2.circle(img, (x3, y3), 10, (0, 255, 0), -1)
            volume = np.interp(length, [30, 200], [0, 100])
            print(length, volume)
            if (volume <= 100) and (volume >= 0):
                call(["amixer", "-D", "pulse", "sset", "Master",
                      str(volume)+"%"], stdout=subprocess.PIPE)
        else:
            cv2.circle(img, (x3, y3), 10, (0, 0, 255), -1)

    cv2.rectangle(img, (50, 200), (85, 400), (255, 0, 0), 3)
    cv2.rectangle(img, (50, 400-int(volume*2)),
                  (85, 400), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volume)}%', (50, 450),
                cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (255, 0, 0), 2)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 50),
                cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 2)

    cv2.imshow('Images', img)
    if cv2.waitKey(1) == ord('q'):
        break
