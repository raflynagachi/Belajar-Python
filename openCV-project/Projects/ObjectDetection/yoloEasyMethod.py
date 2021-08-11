import cv2
import numpy as np

whT = 320
conf_threshold = 0.5
nms_threshold = 0.3
cap = cv2.VideoCapture('Projects/ObjectDetection/Resources/car.mp4')

classesFile = 'Projects/ObjectDetection/Resources/coco.names'
classNames = []
with open(classesFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')
# print(classNames)

modelConfig = 'Projects/ObjectDetection/Resources/yolov3-tiny.cfg'
modelWeights = '/media/nagachi/Nagachi/Datasets/YOLO/yolov3-tiny.weights'

net = cv2.dnn.readNetFromDarknet(modelConfig, modelWeights)
net.setPreferableBackend(cv2.dnn.DNN_BACKEND_OPENCV)
net.setPreferableTarget(cv2.dnn.DNN_TARGET_CPU)


def findObjects(outputs, img):
    hT, wT, cT = img.shape
    bbox = []
    classIds = []
    confs = []

    for output in outputs:
        for detection in output:
            scores = detection[5:]
            classId = np.argmax(scores)
            confidence = scores[classId]
            if confidence > conf_threshold:
                w, h = int(detection[2]*wT), int(detection[3]*hT)
                x, y = int((detection[0]*wT) - w /
                           2), int((detection[1]*hT) - h/2)
                bbox.append([x, y, w, h])
                classIds.append(classId)
                confs.append(float(confidence))
    # print(bbox)
    indices = cv2.dnn.NMSBoxes(bbox, confs, conf_threshold, nms_threshold)
    for i in indices:
        i = i[0]
        box = bbox[i]
        x, y, w, h = box[0], box[1], box[2], box[3]
        cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 255), 2)
        cv2.putText(img, f'{classNames[classIds[i]].upper()} {(confs[i]*100)}%',
                    (x, y-10), cv2.FONT_HERSHEY_PLAIN, 0.6, (255, 0, 255), 2)


while True:
    success, img = cap.read()

    blob = cv2.dnn.blobFromImage(
        img, 1 / 255, (whT, whT), [0, 0, 0], 1, crop=False)
    net.setInput(blob)

    layerNames = net.getLayerNames()
    # print(layerNames)
    outputNames = [layerNames[i[0]-1] for i in net.getUnconnectedOutLayers()]
    # print(outputNames)
    # print(net.getUnconnectedOutLayers())
    output = net.forward(outputNames)
    # print(output[0].shape)
    # print(output[1].shape)
    # print(output[2].shape)

    findObjects(output, img)

    cv2.imshow('Images', img)
    if cv2.waitKey(10) == ord('q'):
        break
