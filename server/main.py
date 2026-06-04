# main.py

from fastapi import FastAPI
from fastapi.responses import HTMLResponse, StreamingResponse

import cv2
from ultralytics import YOLO

app=FastAPI()

@app.get("/")
def home():
    return HTMLResponse("""
        <html>
            <head>
                <style>
                    img{
                        width:800px;
                        }
                </style>
            </head>
            <body>
                <h1> fastapi - docker </h1>
                <p> esp 실시간 분석 </p>
                <img src="/video">
            </body>
        </html>
""")

model = YOLO("yolov8n.pt")
# esp 받아서 보내줄 함수
def get_frames():
    cap = cv2.VideoCapture("http://192.168.0.97:81/stream")
    while True:
        ret, frame = cap.read()
        if not ret:break
        result = model(frame, verbose=False)
        res = result[0].plot()
        sc, buffer = cv2.imencode(".jpg", res)
        if not sc : continue
        yield (
            b"--frame\r\n"
            b"Content-Type: image/jpeg\r\n\r\n"+
            buffer.tobytes() + b"\r\n"
        )
    cap.release()

@app.get("/video")
def video():
    return StreamingResponse(
        get_frames(),
        media_type="multipart/x-mixed-replace; boundary=frame"
    )

@app.get("/info")
def get_info():
    return [
        {
            "id":1, "name":"이순신",
            "age":45
        },
        {
            "id":2, "name":"김유신",
            "age":67
        }
    ]