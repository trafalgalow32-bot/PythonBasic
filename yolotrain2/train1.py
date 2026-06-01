# train1.py

from ultralytics import YOLO

model = YOLO("yolov8n.pt")

model.train(
    data = "data.yaml",
    epochs = 20,
    imgsz = 640,
    batch = 4
)


"""
 yolo 기본 모델 - yolov8n.pt
  yolov8n-seg.pt ( segment - 객체 분할)
  yolov8n-pose.pt ( pose - 관절 인식 )
  yolov8n-cls.pt ( classification - 분류)
  yolov8n-obb.pt ( object oriented bbox)

  yolo 모델들은 기본적으로 엄청 많은 데이터로 학습을 시켜 놓았다. 
  하지만 아무리 많은 데이터로 학습을 시켜도 세상 모든 상황에 대한
  학습은 아니고 학습 되지 않은 대상도 있기 때문에 
  영상분석 개발을 하는 사람들은 추가로 학습을 시켜야 한다.

  보드마카 펜을 제시했을 대 이게 펜이야 사람이야 병이야
  인지를 못하기 때문에 직접 알려줘야 한다.

  AI에게 알려주는 방법은??
   - 학습할 사진 필요
   - 사진 안에서 학습시킬 대상의 위치와 이름

   boardmarker_001.jpg
   boardmarker_001.txt

   yolo 학습 시키기 - 고정 물체인 경우
    필요환 이미지 수 : 최소 30장 (실제로는 수천 수만 )
   
"""