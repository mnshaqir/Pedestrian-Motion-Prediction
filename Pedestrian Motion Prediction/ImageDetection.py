from ultralytics import YOLO
import cv2

model = YOLO('../Yolov8 Model/yolov8n.pt')
result = model("../YOLO with Picture/Images/1.jpg", show=True)

cv2.waitKey(0)


