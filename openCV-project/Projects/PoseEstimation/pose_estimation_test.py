import cv2
import time
import pose_estimation_module as pem

cap = cv2.VideoCapture(0)
pTime, cTime = 0, 0
detector = pem.poseDetector()
while True:
    succes, img = cap.read()
    img = cv2.flip(img, 1)
    detector.findPose(img)
    lmList = detector.findPosition(img)

    if len(lmList) != 0:
        print(lmList)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50),
                cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)
    cv2.imshow('Images', img)

    if cv2.waitKey(1) == ord('q'):
        break
