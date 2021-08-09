import cv2
import mediapipe as mp
import time
import math


class handDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.detectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(
            self.mode, self.maxHands, self.detectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils

        self.tipIds = [4, 8, 12, 16, 20]

    def findHands(self, img, draw=True):
        img = cv2.flip(img, 1)
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(
                        img, handLms, self.mpHands.HAND_CONNECTIONS)
        return img

    def findPosition(self, img, handNo=0, draw=True):
        self.lmList = []

        if self.results.multi_hand_landmarks:
            myHand = self.results.multi_hand_landmarks[handNo]
            h, w, c = img.shape

            for id, lm in enumerate(myHand.landmark):
                # print(id, lm)
                cx, cy = int(lm.x*w), int(lm.y*h)
                # print(id, cx, cy)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.putText(img, str(id), (cx+5, cy+5),
                                cv2.FONT_HERSHEY_COMPLEX_SMALL, 0.5, (255, 0, 255), 1)

        return self.lmList

    def fingersUp(self):
        fingers = []

        # Thumbs
        if self.lmList[self.tipIds[0]][1] < self.lmList[self.tipIds[0]-1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        # 4 fingers
        for id in self.tipIds[1:]:
            if self.lmList[id][2] < self.lmList[id-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        return fingers

    def findDistance(self, finger1, finger2, img, draw=True, r=15, t=3):
        x1, y1 = self.lmList[finger1][1], self.lmList[finger1][2]
        x2, y2 = self.lmList[finger2][1], self.lmList[finger2][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2

        if draw:
            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), t)
            cv2.circle(img, (x1, y1), r, (255, 0, 0), -1)
            cv2.circle(img, (x2, y2), r, (255, 0, 0), -1)
            cv2.circle(img, (cx, cy), r, (255, 0, 0), -1)

        length = math.hypot(x2-x1, y2-y1)
        # print(length)

        return length, img, [x1, y1, x2, y2, cx, cy]


def main():
    pTime, cTime = 0, 0
    cap = cv2.VideoCapture(0)
    detector = handDetector()
    while True:
        success, img = cap.read()
        img = detector.findHands(img)
        lmList = detector.findPosition(img)
        if len(lmList) != 0:
            print(lmList[4])  # thumbs

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70),
                    cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 255), 3)

        cv2.imshow('Hand Tracking', img)
        if cv2.waitKey(1) == ord('q'):
            break


if __name__ == '__main__':
    main()
