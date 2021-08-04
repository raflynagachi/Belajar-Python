import cv2
import mediapipe as mp
import time


class faceDetector():
    def __init__(self, minDetectionCon=0.5):
        self.minDetectionCon = minDetectionCon

        self.mpFaceDetection = mp.solutions.face_detection
        self.mpDraw = mp.solutions.drawing_utils
        self.faceDetection = self.mpFaceDetection.FaceDetection(
            self.minDetectionCon)

    def findFaces(self, img, draw=True):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceDetection.process(imgRGB)
        # print(self.results)
        bboxes = []

        if self.results.detections:
            h, w, c = img.shape
            for id, detection in enumerate(self.results.detections):
                # mpDraw.draw_detection(img, detection)
                # print(id, detection)

                bboxC = detection.location_data.relative_bounding_box
                bbox = int(bboxC.xmin*w), int(bboxC.ymin*h), \
                    int(bboxC.width*w), int(bboxC.height*h)
                bboxes.append([id, bbox, detection.score])

                if draw:
                    # cv2.rectangle(img, bbox, (255, 0, 255), 2)
                    self.fancyDraw(img, bbox)

                    cv2.putText(img, f'{int(detection.score[0]*100)}%',
                                (bbox[0], bbox[1]-20),
                                cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 2)

        return img, bboxes

    def fancyDraw(self, img, bbox, length=30, thickness=5, rectangle_thickness=1):
        x, y, w, h = bbox
        x1, y1 = x+w, y+h

        cv2.rectangle(img, bbox, (255, 0, 255), rectangle_thickness)
        # Top left x,y
        cv2.line(img, (x, y), (x+length, y), (255, 0, 255), thickness)
        cv2.line(img, (x, y), (x, y+length), (255, 0, 255), thickness)

        # Top right x1,y
        cv2.line(img, (x1, y), (x1-length, y), (255, 0, 255), thickness)
        cv2.line(img, (x1, y), (x1, y+length), (255, 0, 255), thickness)

        # Bottom left x,y1
        cv2.line(img, (x, y1), (x+length, y1), (255, 0, 255), thickness)
        cv2.line(img, (x, y1), (x, y1-length), (255, 0, 255), thickness)

        # Bottom right x1,y1
        cv2.line(img, (x1, y1), (x1-length, y1), (255, 0, 255), thickness)
        cv2.line(img, (x1, y1), (x1, y1-length), (255, 0, 255), thickness)


def main():
    cap = cv2.VideoCapture(0)
    cTime, pTime = 0, 0
    detector = faceDetector()
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


if __name__ == '__main__':
    main()
