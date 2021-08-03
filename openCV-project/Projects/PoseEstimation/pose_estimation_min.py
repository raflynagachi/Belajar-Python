import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture(0)
pTime, cTime = 0, 0

while True:
    succes, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = pose.process(imgRGB)

    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks,
                              mpPose.POSE_CONNECTIONS)
        h, w, c = img.shape
        for id, lm in enumerate(results.pose_landmarks.landmark):
            cx, cy = int(lm.x*w), int(lm.y*h)
            print([id, cx, cy])
            cv2.putText(img, str(id), (cx+5, cy+5),
                        cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0, 255, 0), 1)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (70, 50),
                cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 255), 3)
    cv2.imshow('Images', img)

    if cv2.waitKey(1) == ord('q'):
        break
