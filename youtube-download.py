import shutil
import time

from tkinter import *
from moviepy.editor import *
import pytube

# Functions


def download_video():
    video_url = url.get()
    try:
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.first()
        video.download("C:/Users/Lee/Desktop/Videos")
        notif.config(fg="green", text="Download video success")
    except Exception as e:
        print(e)
        notif.config(fg="red", text="Video could not be downloaded")


def download_mp3():
    video_url = url.get()
    try:
        mp4 = pytube.YouTube(video_url).streams.first().download()
        mp3 = mp4.split(".mp4", 1)[0] + f".mp3"

        start_time = time.time()
        print("Converting...")

        video_clip = VideoFileClip(mp4)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(mp3)

        print(f"Time elapsed: {time.time() - start_time} seconds")
        audio_clip.close()
        video_clip.close()

        os.remove(mp4)

        shutil.move(mp3, r"C:/Users/Lee/Desktop/MP3")
        notif.config(fg="green", text="Download video success")
    except Exception as e:
        print(e)
        notif.config(fg="red", text="Video could not be downloaded")


# Main Screen
master = Tk()
master.title("Youtube Video Downloader")


# Labels
Label(master, text="Youtube Video Converter", fg="blue",
      font=("Calibri", 16)).grid(sticky=N, padx=100, row=0)

Label(master, text="Enter the youtube link below :",
      font=("Calibri", 12)).grid(sticky=N, pady=15, row=1)

# Notification
notif = Label(master, font=("Calibri", 12))
notif.grid(sticky=N, pady=1, row=5)

# Variables
url = StringVar()

# Entry/Input
Entry(master, width=50, textvariable=url).grid(sticky=N, row=2)

# Button
Button(master, width=20, text="Download Video", fg="green", bg="light yellow",
       font=("Calibri", 12), command=download_video).grid(sticky=N, pady=10, row=3)

Button(master, width=20, text="Download MP3", fg="green", bg="light yellow",
       font=("Calibri", 12), command=download_mp3).grid(sticky=N, pady=10, row=4)
# Loop
master.mainloop()
