import cv2
import hands_detector

cap = cv2.VideoCapture(0)

while True:
    ret, src = cap.read()
    if not ret:
        break
    det = hands_detector.detect(src)
    if det is not None:
        dst = hands_detector.draw_boxes(src, det)
    else:
        dst = src.copy()
    cv2.imshow('dst', dst)
    key = cv2.waitKey(1)
    if key == ord('q'):
        break