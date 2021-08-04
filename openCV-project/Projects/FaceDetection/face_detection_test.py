import cv2
import time
import face_detection_module as fdm

cap = cv2.VideoCapture(0)
cTime, pTime = 0, 0
detector = fdm.faceDetector()
while True:
    isTrue, img = cap.read()
    img = cv2.flip(img, 1)
    img, bboxes = detector.findFaces(img)
    print(bboxes)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {str(int(fps))}', (20, 70),
                cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.imshow('Images', img)

    if cv2.waitKey(1) == ord('q'):
        break
