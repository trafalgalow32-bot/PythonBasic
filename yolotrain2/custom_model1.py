# custom_model1.py

import cv2
from pathlib import Path
from ultralytics import YOLO

model = YOLO("./runs/detect/train-2/weights/best.pt")

cap = cv2.VideoCapture(0) # "http://192.168.0.97:81/stream"

while True:
    ret, frame = cap.read()
    if not ret: break 
    result = model(frame)
    res = result[0].plot()
    cv2.imshow("marker", res)
    if cv2.waitKey(1) == 27:break
cap.release()
cv2.destroyAllWindows()