from tkinter import *
import pytube

# Functions


def download():
    video_url = url.get()
    try:
        youtube = pytube.YouTube(video_url)
        video = youtube.streams.first()
        video.download("C:/Users/Lee/Desktop/Videos")
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
notif.grid(sticky=N, pady=1, row=4)

# Variables
url = StringVar()

# Entry/Input
Entry(master, width=50, textvariable=url).grid(sticky=N, row=2)

# Button
Button(master, width=20, text="Download", fg="green", bg="light yellow",
       font=("Calibri", 12), command=download).grid(sticky=N, pady=20, row=3)
# Loop
master.mainloop()
