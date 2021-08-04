import cv2
import mediapipe as mp
import time

mpFaceDetection = mp.solutions.face_detection
mpDraw = mp.solutions.drawing_utils
faceDetection = mpFaceDetection.FaceDetection()

cap = cv2.VideoCapture(0)
cTime, pTime = 0, 0

while True:
    isTrue, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    # print(results)

    if results.detections:
        h, w, c = img.shape
        for id, detection in enumerate(results.detections):
            # mpDraw.draw_detection(img, detection)
            # print(id, detection)

            bboxC = detection.location_data.relative_bounding_box
            bbox = int(bboxC.xmin*w), int(bboxC.ymin*h), \
                int(bboxC.width*w), int(bboxC.height*h)
            cv2.rectangle(img, bbox, (255, 0, 0), 2)
            cv2.putText(img, f'{int(detection.score[0]*100)}%', (bbox[0], bbox[1]-20),
                        cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {str(int(fps))}', (20, 70),
                cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)
    cv2.imshow('Images', img)

    if cv2.waitKey(1) == ord('q'):
        break
