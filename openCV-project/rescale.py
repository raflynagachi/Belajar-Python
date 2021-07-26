import cv2


def rescaleFrame(frame, scale=.75):
    # work for images, videos and live videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)

    return cv2.resize(frame, dimensions, interpolation=cv2.INTER_AREA)


def changeSize(capture, width, height):
    # only work for live video

    # 3 & 4 is width and height properties index
    # in VideoCapture properties
    capture.set(3, width)
    capture.set(4, height)


# Rescale images
# img = cv2.imread('Resources/Photos/cat.jpg')
# img = rescaleFrame(img)
# cv2.imshow('Cat', img)

# Rescale videos
webcam = cv2.VideoCapture(0)
changeSize(webcam, 144, 78)

while webcam.isOpened():
    isTrue, frame = webcam.read()

    if isTrue:
        frame_resized = rescaleFrame(frame, 1)  # Rescale
        frame_resized = cv2.flip(frame_resized, 1)  # Flip horizontal
        cv2.imshow('Video', frame_resized)

    if cv2.waitKey(1) == ord('q'):  # abort key
        break

webcam.release()
cv2.destroyAllWindows()
