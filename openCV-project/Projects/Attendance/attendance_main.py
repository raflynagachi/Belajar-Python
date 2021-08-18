import cv2
import numpy as np
import face_recognition

img = face_recognition.load_image_file(
    'Resources/Faces/train/Ben Afflek/1.jpg')
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

img_test = face_recognition.load_image_file(
    'Resources/Faces/train/Ben Afflek/3.jpg')
img_test = cv2.cvtColor(img_test, cv2.COLOR_BGR2RGB)

faceloc = face_recognition.face_locations(img)[0]
encode = face_recognition.face_encodings(img)[0]
cv2.rectangle(img, (faceloc[3], faceloc[0]),
              (faceloc[1], faceloc[2]), (0, 255, 0), 2)

faceloc_test = face_recognition.face_locations(img_test)[0]
encode_test = face_recognition.face_encodings(img_test)[0]
cv2.rectangle(img_test, (faceloc_test[3], faceloc_test[0]),
              (faceloc_test[1], faceloc_test[2]), (0, 255, 0), 2)

# print(faceloc)
# print('=================================')
# print(encode)

cv2.imshow('Images', img)
cv2.imshow('Images_test', img_test)
cv2.waitKey()
