import os
from tkinter import filedialog
import tkinter as tk

def select_video():
    root = tk.Tk()
    root.withdraw()

    video_file_path = filedialog.askopenfilename(
        title="Select Video",
        filetypes=(("Video files", "*.mp4;*.avi"), ("All files", "*.*"))
    )

    return video_file_path

def run_video(video_path):
    # Open the video file with the default media player
    os.startfile(video_path)

# Example usage
selected_video = select_video()
if selected_video:
    run_video(selected_video)
