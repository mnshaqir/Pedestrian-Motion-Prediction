import tkinter as tk
from PIL import ImageTk
from tkinter import filedialog
from tkinter import *
import sys
import os

bg_colour = "cyan"
def clear_widgets(frame):
    for widget in frame.winfo_children():
        widget.destroy()

def run_VideoDetection():
    os.system('VideoDetection.py')

def run_WebcamDetection():
    os.system('WebcamDetection.py')

def run_ImageDetection():
    os.system('ImageDetection.py')

def load_frame1():
    clear_widgets(frame2)
    frame1.tkraise()
    frame1.pack_propagate(False)
    # frame1 widgets
    logo_img = ImageTk.PhotoImage(file="../YOLO with Video/Images/logo.png")
    logo_widget = tk.Label(frame1, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack()

    tk.Label(frame1,
                     text=" Let's make some detections !",
                     bg=bg_colour,
                     fg="black",
                     font=("TkMenuFont", 15)
                     ).pack()


    # button widget
    tk.Button(frame1,
                       text="Try now",
                       font=("TkHeadingFont", 17),
                       bg="#A2A2B5",
                       fg="black",
                       cursor="hand2",
                       activebackground="#FFFFFA",
                       activeforeground="black",
                       command=lambda: load_frame2()
                       ).pack(pady=5)

def load_frame2():
    clear_widgets(frame1)
    frame2.tkraise()
    logo_img = ImageTk.PhotoImage(file="../YOLO with Video/Images/Gambar logo 1.png")
    logo_widget = tk.Label(frame2, image=logo_img, bg=bg_colour)
    logo_widget.image = logo_img
    logo_widget.pack(pady=20)

# for Images detection
    label1 = tk.Label(frame2,
                      text="Images Detection",
                      bg=bg_colour,
                      fg="black",
                      font=("TkHeadingFont", 15))
    label1.place(x=95, y=410)

    button1 = tk.Button(frame2,
                        text="Images",
                        font=("TkHeadingFont", 17),
                        bg="#A2A2B5",
                        fg="black",
                        cursor="hand2",
                        activebackground="#777788",
                        activeforeground="black",
                        command=lambda: run_ImageDetection())
    button1.place(x=125, y=450, width=100, height=40)

# for Webcam detection
    label2 = tk.Label(frame2,
                      text="Webcam Detection",
                      bg=bg_colour,
                      fg="black",
                      font=("TkHeadingFont", 15))
    label2.place(x=280, y=410)

    button2 = tk.Button(frame2,
                        text="Webcam",
                        font=("TkHeadingFont", 17),
                        bg="#A2A2B5",
                        fg="black",
                        cursor="hand2",
                        activebackground="#777788",
                        activeforeground="black",
                        command=lambda: run_WebcamDetection())
    button2.place(x=310, y=450, width=110, height=40)

# for Video detection
    label3 = tk.Label(frame2,
                      text="Video Detection",
                      bg=bg_colour,
                      fg="black",
                      font=("TkHeadingFont", 15))
    label3.place(x=500, y=410)

    button3 = tk.Button(frame2,
                        text="Video",
                        font=("TkHeadingFont", 17),
                        bg="#A2A2B5",
                        fg="black",
                        cursor="hand2",
                        activebackground="#777788",
                        activeforeground="black",
                        command=lambda: run_VideoDetection())
    button3.place(x=510, y=450, width=110, height=40)

# for back button
    button4 = tk.Button(frame2,
                        text="<",
                        font=("TkHeadingFont", 12),
                        bg="#DEDEDE",
                        fg="black",
                        cursor="hand2",
                        activebackground="#DEDEDE",
                        activeforeground="black",
                        command=lambda: load_frame1())
    button4.place(x=0, y=0)

    # print("Active")

# initialize app
root = tk.Tk()
root.title("Pedestrian Motion Prediction")
# root.eval("tk::PlaceWindow . center")

# place app at the center of the screen
# x = root.winfo_screenwidth() // 2
# y = int(root.winfo_screenheight() * 0.1)
# root.geometry('800x600+' + str(x) + '+' + str(y))  # size & location of window

# create a frame widget
frame1 = tk.Frame(root, width=600, height=600, bg=bg_colour)
frame2 = tk.Frame(root, bg=bg_colour)

for frame in (frame1, frame2):
    frame.grid(row=0, column=0)
    frame.grid(row=0, column=0, sticky="nesw")  # expand

load_frame1()
# run app
root.mainloop()
