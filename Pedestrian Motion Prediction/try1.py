import tkinter as tk
from tkinter import filedialog
import numpy as np
from ultralytics import YOLO
import cv2
from cv2 import INTER_AREA
import cvzone
import math
from sort import *
from gui_buttons import Buttons

def select_video():
    root = tk.Tk()
    root.withdraw()

    video_file_path = filedialog.askopenfilename(
        title="Select Video",
        filetypes=(("Video files", "*.mp4;*.avi"), ("All files", "*.*"))
    )

    return video_file_path

def process_selected_video():
    selected_video = select_video()

    # Perform actions with the selected video

    # Initialize Buttons
    button = Buttons()
    button.add_button("Person", 20, 20)
    button.add_button("Car", 165, 20)
    button.add_button("Motorbike", 250, 20)
    button.add_button("Bus", 448, 20)

    # for video
    def input_videos():
        cv2.VideoCapture("process_selected_video")
    cap = input_videos()

    # cap = cv2.VideoCapture("../Yolo with Video/Video/16th.mp4")

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

    # for webcam
    # cap = cv2.VideoCapture(0)
    # cap.set(3, 1280)
    # cap.set(4, 720)

    model = YOLO("../Yolov8 Model/yolov8n.pt")

    classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck",
                  "boat", "traffic light", "fire hydrant", "stop sign", "parking meter", "bench",
                  "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe",
                  "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard",
                  "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard", "tennis racket",
                  "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich",
                  "orange", "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "potted plant",
                  "bed", "dining table", "toilet", "tv", "monitor", "laptop", "mouse", "remote", "cell phone",
                  "keyboard",
                  "microwave",
                  "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors", "teddy bear",
                  "hair dryer", "toothbrush"]

    tracker = Sort(max_age=10, min_hits=3, iou_threshold=0.3)

    # ( x1, y1 , x2, y2)
    # 1st video scale = 1 *
    # limitsLeft = [200, 450, 200, 750]
    # limitsRight = [1000, 450, 1000, 750]
    # # 2nd video scale = 0.3 *
    # limitsLeft = [250, 600, 250, 350]
    # limitsRight = [900, 600, 900, 350]
    # 3rd video scale = 0.3 *
    # limitsLeft = [250, 450, 250, 250]
    # limitsRight = [900, 450, 900, 250]
    # 4th video scale = 1.5
    # limitsLeft = [150, 450, 150, 250]
    # limitsRight = [800, 450, 800, 250]
    # 5th video scale = 0.5
    # limitsLeft = [200, 700, 200, 450]
    # limitsRight = [850, 700, 850, 450]
    # 6th video scale = 0.3
    # limitsLeft = [100, 600, 100, 300]
    # limitsRight = [800, 600, 800, 300]
    # 7th video scale = 1
    # limitsLeft = [100, 450, 400, 500]
    # limitsRight = [300, 250, 700, 270]
    # 8th video scale = 0.5
    # limitsLeft = [250, 550, 250, 350]
    # limitsRight = [700, 500, 700, 350]
    # 9th video scale = 0.5
    # limitsLeft = [250, 250, 250, 500]
    # limitsRight = [500, 250, 500, 450]
    # 10th video scale = 1
    # limitsLeft = [500, 450, 500, 750]
    # limitsRight = [900, 450, 900, 750]
    # 11th video scale = 1.5
    # limitsLeft = [300, 500, 300, 200]
    # limitsRight = [850, 500, 850, 200]
    # 12th video scale = 0.3
    # limitsLeft = [100, 600, 100, 250]
    # limitsRight = [850, 600, 850, 250]
    # 13th video scale = 1
    # limitsLeft = [500, 600, 500, 300]
    # limitsRight = [950, 600, 950, 300]
    # 14th video scale = 1.5
    # limitsLeft = [300, 500, 300, 200]
    # limitsRight = [850, 500, 850, 200]
    # 15th video scale = 1.5
    # limitsLeft = [200, 500, 200, 100]
    # limitsRight = [750, 500, 750, 100]
    # 16th video scale = 1
    limitsLeft = [100, 700, 100, 450]
    limitsRight = [850, 700, 850, 450]
    # 17th video scale = 2
    # limitsLeft = [250, 750, 250, 450]
    # limitsRight = [1000, 800, 1000, 450]
    # 18th video scale = 1
    # limitsLeft = [300, 700, 300, 450]
    # limitsRight = [1050, 700, 1050, 450]
    # 19th video scale = 1
    # limitsLeft = [300, 700, 300, 450]
    # limitsRight = [1050, 700, 1050, 450]
    # 20th video scale = 1.5
    # limitsLeft = [200, 500, 200, 250]
    # limitsRight = [750, 500, 750, 250]

    totalCount = []

    while True:
        # Get frames
        success, frame = cap.read()
        # overlay images
        # imgGraphics = cv2.imread("../Yolo with Video/Images/Attention_2.png", cv2.IMREAD_UNCHANGED)
        # frame = cvzone.overlayPNG(frame, imgGraphics, (800, 60))
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

                # Detect All
                # cv2.rectangle(resize_frame, (x1, y1), (x2, y2), (255, 0, 0), 3)
                # print(x1, y1, x2, y2)

                # cvZoneRectangle
                w, h = x2 - x1, y2 - y1

                # confidence
                conf = math.ceil((box.conf[0] * 100)) / 100
                # class names
                cls = int(box.cls[0])
                currentClass = classNames[cls]

                # if currentClass == "person" or currentClass == "car" or currentClass == "bus" and conf >= 0.5:
                if currentClass in active_buttons:
                    if currentClass == "person" or currentClass == "car" or currentClass == "bus" or \
                            currentClass == "motorbike" and conf >= 0.5:
                        cvzone.cornerRect(resize_frame, (x1, y1, w, h), l=9, rt=3)
                        currentArray = np.array([x1, y1, x2, y2, conf])
                        detections = np.vstack((detections, currentArray))

                    # show name & confidence
                    # cvzone.putTextRect(resize_frame, f'{currentClass} {conf}', (max(0, x1), max(35, y1)),
                    #                   scale=0.6, thickness=1, offset=3)
                    # cvzone.cornerRect(resize_frame, (x1, y1, w, h), l=9, rt=3)

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

            # if currentClass == "person" and button_person is True:
            # if currentClass in active_buttons:
            cvzone.cornerRect(resize_frame, (x1, y1, w, h), l=9, rt=2, colorR=(255, 0, 0))
            cvzone.putTextRect(resize_frame, f' {int(id)}', (max(0, x1), max(35, y1)), scale=2,
                               thickness=2, offset=3)

            cx, cy = x1 + w // 2, y1 + h // 2
            cv2.circle(resize_frame, (cx, cy), 5, (0, 0, 255), cv2.FILLED)
            # totalCount += 1
            # for 7th video
            # if limitsLeft[0] < cx < limitsLeft[2] and limitsLeft[1] - 15 < cy < limitsLeft[1] + 15:
            if limitsLeft[0] - 5 < cx < limitsLeft[2] + 5 or limitsLeft[1] - 30 < cy < limitsLeft[1] + 30:
                if totalCount.count(id) == 0:
                    # cvzone.putTextRect(resize_frame, 'WARNING !!!', (700, 50))
                    totalCount.append(id)

            # cv2.line(resize_frame, (limitsLeft[0], limitsLeft[1]), (limitsLeft[2], limitsLeft[3]), (0, 255, 0), 5)
            # for 7th video
            # if limitsRight[0] < cx < limitsRight[2] and limitsRight[1] - 0.6 < cy < limitsRight[1] + 0.6:
            if limitsRight[0] - 5 < cx < limitsRight[2] + 5 or limitsRight[1] - 30 < cy < limitsRight[1] + 30:
                if totalCount.count(id) == 0:
                    # cvzone.putTextRect(resize_frame, 'WARNING !!!', (700, 50))
                    # cvzone.putTextRect(resize_frame, f' Count: {len(totalCount)}', (700, 50))
                    # else:
                    #     print()
                    totalCount.append(id)

        cvzone.putTextRect(resize_frame, f' Count: {len(totalCount)}', (700, 50))
        # cvzone.putTextRect(resize_frame, f'{len(totalCount)}', (700, 50))
        # cvzone.overlayPNG(resize_frame, imgGraphics,(700, 50))
        # cvzone.putTextRect(resize_frame, f' Count {cy} ', (50, 50))
        # cv2.putText(resize_frame, str(len(totalCount)), (700, 50), cv2.FONT_HERSHEY_PLAIN, 5, (50, 50, 255), 8)

        # create button
        # polygon1 = np.array([[(20, 35), (150, 35), (150, 65), (20, 65)]])
        # cv2.fillPoly(resize_frame, polygon1, (0, 0, 200))
        # cv2.putText(resize_frame, "Person", (30, 60), cv2.FONT_HERSHEY_PLAIN, 2, (255, 255, 255), 2)

        # Display button
        button.display_buttons(resize_frame)

        cv2.imshow("Pedestrian Motion Prediction", resize_frame)
        key = cv2.waitKey(0)
        if key == 27:
            break
    cap.release()
    cv2.destroyAllWindows()

    print("Selected video:", selected_video)

# Call the function that utilizes the video selection code
process_selected_video()
