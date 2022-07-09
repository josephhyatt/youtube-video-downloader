import shutil
from email.mime import image
from tkinter import *
from tkinter import filedialog

from moviepy import *
from moviepy.editor import VideoFileClip
from pytube import YouTube


# functions
def select_path():
    # allows user to select a path from the explorer
    path = filedialog.askdirectory()
    path_label.config(text=path)


def download_file():
    # get user path
    get_link = link_field.get()
    # get selected path
    user_path = path_label.cget("text")
    screen.title("Downloading...")
    # download video
    # mp4_video = YouTube(get_link).streams.get_highest_resolution().download()
    mp4_video = YouTube(get_link).streams.order_by("resolution").desc()[0].download()
    vid_clip = VideoFileClip(mp4_video)
    vid_clip.close()
    # moves file to selected directory
    shutil.move(mp4_video, user_path)
    screen.title("Download Complete. Download another file...")


# ui
screen = Tk()
title = screen.title("Youtube Download")
canvas = Canvas(screen, width=500, height=500)
canvas.pack()

# image logo
logo_img = PhotoImage(file="yt.png")

# resize image
logo_img = logo_img.subsample(2, 2)
canvas.create_image(250, 100, image=logo_img)

# link field (widgets)
link_field = Entry(screen, width=50)
link_label = Label(screen, text="Enter Youtube URL: ", font=("Arial", 15))

# select path for saved files
path_label = Label(screen, text="Select Path for Download", font=("Arial", 15))
select_btn = Button(screen, text="Select", command=select_path)

# add button to window
canvas.create_window(250, 300, window=path_label)
canvas.create_window(250, 360, window=select_btn)

# add widgets to window
canvas.create_window(250, 210, window=link_label)
canvas.create_window(250, 250, window=link_field)

# download button
download_btn = Button(screen, text="Download File", command=download_file)

# add to canvas
canvas.create_window(250, 420, window=download_btn)

screen.mainloop()
