from tkinter import *
from pytube import YouTube
from tkinter import messagebox

# Youtube video download user interface


root = Tk()
root.title("Youtube Video Downloader")
root.iconbitmap("c:/Icons/ui.ico")


# Commands


def download_link(link):
    global video_link
    global label_link
    video_link = link


def download_path(path):
    global video_path
    global label_path
    video_path = path


def show_qualities():
    global video_link
    global video_path
    global streams
    global dict_streams

    try:
        if "/" not in video_path or "youtube" in video_path:
            messagebox.showwarning("Warning", "Invalid path")
        if "youtube" not in video_link:
            messagebox.showwarning("Warning", "Invalid link")

        yt = YouTube(video_link)
        # appends all of the items to streams list
        streams = streams[1:]
        for n, i in enumerate(yt.streams.all(), start=1):
            streams.append(str(n) + ". " + str(i))
            dict_streams[str(n)] = i
        # which will be displayed in stream option menu
        stream_new = OptionMenu(root, option, *streams)
        stream_new.grid(row=1, column=3)
        # Download available
        download_button_new = Button(text="Download", command=lambda: download(option.get()), state=NORMAL)
        download_button_new.grid(row=4, column=2)
    except NameError:
        messagebox.showerror("Error", "Fill input fields")


def download(value):
    global video_link
    global video_path
    global dict_streams

    Label(root, text="downloading...").grid(row=4, column=3)
    dict_streams.get(value.split(".")[0]).download(video_path)
    Label(root, text="Downloaded").grid(row=4, column=3)

# variables

dict_streams = {}
streams = ["Different video formats and qualities"]
option = StringVar()

# Dropdown boxes


stream = OptionMenu(root, option, *streams)

# Input fields


link_field = Entry(root, width=50, borderwidth=30)
path_field = Entry(root, width=50, borderwidth=30)

# Define buttons


confirm_link = Button(text="Confirm Link", command=lambda: download_link(link_field.get()))
confirm_path = Button(text="Confirm Path", command=lambda: download_path(path_field.get()))
confirm_button = Button(text="Confirm", command=show_qualities)
download_button = Button(text="Download", command=download, state=DISABLED)

# Geometry manager


stream.grid(row=1, column=3)
link_field.grid(row=0, column=0, columnspan=3)
path_field.grid(row=2, column=0, columnspan=3)
confirm_link.grid(row=1, column=1)
confirm_path.grid(row=3, column=1)
confirm_button.grid(row=4, column=1)
download_button.grid(row=4, column=2)

root.mainloop()
