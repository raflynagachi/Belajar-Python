import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpFaceMesh = mp.solutions.face_mesh
faceMesh = mpFaceMesh.FaceMesh(max_num_faces=1)
drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=2)

cap = cv2.VideoCapture(0)
pTime = 0
while True:
    succes, img = cap.read()
    img = cv2.flip(img, 1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceMesh.process(imgRGB)

    if results.multi_face_landmarks:
        h, w, c = img.shape
        for faceLms in results.multi_face_landmarks:
            mpDraw.draw_landmarks(
                img, faceLms, mpFaceMesh.FACE_CONNECTIONS, drawSpec, drawSpec)

            for id, lm in enumerate(faceLms.landmark):
                x, y = int(lm.x*w), int(lm.y*h)
                print([id, x, y])

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    cv2.putText(img, f'FPS: {int(fps)}', (20, 70),
                cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

    cv2.imshow('Images', img)

    if cv2.waitKey(1) == ord('q'):
        break
