import numpy as np
from ultralytics import YOLO
import cv2
from cv2 import INTER_AREA
import cvzone
import math
from sort import *
from gui_buttons import Buttons

# Initialize Buttons
button = Buttons()
button.add_button("Person", 20, 20)
button.add_button("Car", 165, 20)
button.add_button("Motorbike", 250, 20)
button.add_button("Bus", 448, 20)

# for webcam
cap = cv2.VideoCapture(0)
cap.set(3, 1280)
cap.set(4, 720)

def resized(frame, scale=1):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimension = (width, height)
    return cv2.resize(frame, dimension, interpolation=cv2.INTER_AREA)


# button_person = False


def click_button(event, x, y, flags, params):
    # global button_person
    if event == cv2.EVENT_LBUTTONDOWN:
        button.button_click(x, y)


# create window
cv2.namedWindow("Pedestrian Motion Prediction")
cv2.setMouseCallback("Pedestrian Motion Prediction", click_button)


model = YOLO("../Yolov8 Model/yolov8l.pt")

classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck",
              "boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench",
              "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe",
              "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard",
              "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket",
              "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich",
              "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "potted plant",
              "bed", "dining table", "toilet", "tv", "monitor", "laptop", "mouse", "remote", "cell phone", "keyboard",
              "microwave",
              "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors", "teddy bear",
              "hair dryer", "toothbrush"]

tracker = Sort(max_age=10, min_hits=3, iou_threshold=0.3)

# ( x1, y1 , x2, y2)
# 1st video scale = 1 *
limitsLeft = [100, 150, 100, 750]
limitsRight = [1100, 150, 1100, 750]


totalCount = []

while True:
    # Get frames
    success, frame = cap.read()
    # Resize Video
    resize_frame = resized(frame)
    result = model(resize_frame, stream=True)
    detections = np.empty((0, 5))
    # Active Button
    active_buttons = button.active_buttons_list()
    print("Active buttons", active_buttons)

    for r in result:
        boxes = r.boxes
        for box in boxes:
            # bounding boxes
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)

            # cvZoneRectangle
            w, h = x2 - x1, y2 - y1

            # confidence
            conf = math.ceil((box.conf[0] * 100)) / 100
            # class names
            cls = int(box.cls[0])
            currentClass = classNames[cls]

            if currentClass in active_buttons:
                if currentClass == "person" or currentClass == "car" or currentClass == "bus" or \
                        currentClass == "motorbike" and conf >= 0.5:
                    cvzone.cornerRect(resize_frame, (x1, y1, w, h), l=9, rt=3)
                    currentArray = np.array([x1, y1, x2, y2, conf])
                    detections = np.vstack((detections, currentArray))

    resultTracker = tracker.update(detections)
    # line
    cv2.line(resize_frame, (limitsLeft[0], limitsLeft[1]), (limitsLeft[2], limitsLeft[3]), (0, 0, 255), 5)
    cv2.line(resize_frame, (limitsRight[0], limitsRight[1]), (limitsRight[2], limitsRight[3]), (0, 0, 255), 5)

    for result in resultTracker:
        x1, y1, x2, y2, id = result
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        print(result)
        # bbox
        w, h = x2 - x1, y2 - y1


        cvzone.cornerRect(resize_frame, (x1, y1, w, h), l=9, rt=2, colorR=(255, 0, 0))
        cvzone.putTextRect(resize_frame, f' {int(id)}', (max(0, x1), max(35, y1)), scale=2,
                           thickness=2, offset=3)

        cx, cy = x1 + w // 2, y1 + h // 2
        cv2.circle(resize_frame, (cx, cy), 5, (0, 0, 255), cv2.FILLED)

        if limitsLeft[0] - 5 < cx < limitsLeft[2] + 5 or limitsLeft[1] - 30 < cy < limitsLeft[1] + 30:
            if totalCount.count(id) == 0:
                totalCount.append(id)


        if limitsRight[0] - 5 < cx < limitsRight[2] + 5 or limitsRight[1] - 30 < cy < limitsRight[1] + 30:
            if totalCount.count(id) == 0:
                totalCount.append(id)

    cvzone.putTextRect(resize_frame, f' Count: {len(totalCount)}', (700, 50))


    # Display button
    button.display_buttons(resize_frame)

    cv2.imshow("Pedestrian Motion Prediction", resize_frame)
    key = cv2.waitKey(2)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()
