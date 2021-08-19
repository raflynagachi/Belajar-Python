import cv2
import numpy as np
import face_recognition
import os
from datetime import datetime

path = 'Resources/Faces/train'
images = []
classNames = []
for dir in os.listdir(path):
    for image in os.listdir(path+'/'+dir):
        img = cv2.imread(path+'/'+dir+'/'+image)
        images.append(img)
        classNames.append(dir)
        break


def encodings(images):
    encodeList = []
    for i, img in enumerate(images):
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)
        if len(encode) > 0:
            # focus on one face
            encode = encode[0]
            encodeList.append(encode)
        else:
            images.pop(i)
            classNames.pop(i)
    return encodeList


def markAttendance(name):
    with open('Projects/Attendance/attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            date_str = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{date_str}')


print('Encoding...')
encoded_list = encodings(images)
print('Encoding complete...')

cap = cv2.VideoCapture(0)

while True:
    success, img = cap.read()
    img = cv2.flip(img, 1)
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    face_loc = face_recognition.face_locations(imgS)
    face_encode = face_recognition.face_encodings(imgS, face_loc)

    for encodeFace, faceLoc in zip(face_encode, face_loc):
        matches = face_recognition.compare_faces(encoded_list, encodeFace)
        face_dist = face_recognition.face_distance(encoded_list, encodeFace)
        # print(face_dist)

        match_index = np.argmin(face_dist)

        if matches[match_index]:
            name = classNames[match_index].upper()
            print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1*4, x2*4, y2*4, x1*4
            cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.rectangle(img, (x1, y2-35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, name, (x1+6, y2-6),
                        cv2.FONT_HERSHEY_PLAIN, 1, (255, 255, 255), 1)
            markAttendance(name)

    cv2.imshow('Images', img)
    if cv2.waitKey(1) == ord('q'):
        break
