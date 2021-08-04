import cv2
import mediapipe as mp
import time


class poseDetector():
    def __init__(self, mode=False, upperBody=False, smooth=True,
                 detectionCon=0.5, trackingCon=0.5):
        self.mode = mode
        self.upperBody = upperBody
        self.smooth = smooth
        self.detectionCon = detectionCon
        self.trackingCon = trackingCon

        self.mpDraw = mp.solutions.drawing_utils
        self.mpPose = mp.solutions.pose
        self.pose = self.mpPose.Pose(
            self.mode, self.upperBody, self.smooth, self.detectionCon, self.trackingCon)

    def findPose(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(imgRGB)
        if self.results.pose_landmarks:
            if draw:
                self.mpDraw.draw_landmarks(img, self.results.pose_landmarks,
                                           self.mpPose.POSE_CONNECTIONS)

    def findPosition(self, img, draw=True):
        lmList = []
        if self.results.pose_landmarks:
            h, w, c = img.shape
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                cx, cy = int(lm.x*w), int(lm.y*h)
                # print([id, cx, cy])
                lmList.append([id, cx, cy])
                if draw:
                    cv2.putText(img, str(id), (cx+5, cy+5),
                                cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.7, (0, 255, 0), 1)
        return lmList


def main():
    cap = cv2.VideoCapture(0)
    pTime, cTime = 0, 0
    detector = poseDetector()
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


if __name__ == '__main__':
    main()
