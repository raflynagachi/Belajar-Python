import cv2

# img = cv2.imread('Resources/Photos/group 1.jpg')

# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# haar_cascade = cv2.CascadeClassifier('haar.xml')
# faces_rect = haar_cascade.detectMultiScale(
#     gray, scaleFactor=1.1, minNeighbors=2)

# print(f'Number of faces: {len(faces_rect)}')

# for (x, y, w, h) in faces_rect:
#     cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

# cv2.imshow('Images', img)

cam = cv2.VideoCapture(0)

while True:
    isTrue, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    haar_cascade = cv2.CascadeClassifier('haar.xml')
    faces_rect = haar_cascade.detectMultiScale(
        gray, scaleFactor=1.1, minNeighbors=2)

    print(f'Number of faces: {len(faces_rect)}')

    for (x, y, w, h) in faces_rect:
        cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

    cv2.imshow('App', img)
    if cv2.waitKey(1) == ord('q'):
        break
