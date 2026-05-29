# esp_cam1.py

import cv2
from ultralytics import YOLO

model = YOLO("yolov8n.pt")

cap = cv2.VideoCapture("http://192.168.0.97:81/stream") # 내 꺼 주소 찾기(연결되고!)

width = int( cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int( cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
fourcc = cv2.VideoWriter_fourcc(*"mp4v")
writer = cv2.VideoWriter(
    "Yolo/videos/esp_cam1.mp4", fourcc, fps, (width, height)
)


while True:
    ret, frame = cap.read()
    if not ret:break
    frame = cv2.resize( frame, (320, 240))

    result = model(frame)
    res = result[0].plot()
    writer.write(res)    
    cv2.imshow("eap", res)
    if cv2.waitKey(1)==27: break

writer.release()
cap.release()
cv2.destroyAllWindows()