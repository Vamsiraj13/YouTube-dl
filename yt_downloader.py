# Importing necessary packages
import tkinter as tk
from tkinter import *
from pytube import YouTube
from tkinter import messagebox, filedialog
 
 
# Defining CreateWidgets() function
# to create necessary tkinter widgets
def Widgets():
 
    head_label = Label(root, text="Pykinter",
                       padx=15,
                       pady=15,
                       font="Georgia 18",
                       bg="#D9D8D7",
                       fg="black")
    head_label.place(x=240 ,y=20)
 
    link_label = Label(root,
                       text="YouTube link:",
                       bg="salmon",
                       pady=5,
                       padx=5)
    link_label.place(x=40 ,y=84)
 
    root.linkText = Entry(root,
                          width=35,
                          textvariable=video_Link,
                          font="Arial 14")
    root.linkText.place(x=140 ,y=87)
 
 
    destination_label = Label(root,
                              text="Destination:",
                              bg="salmon",
                              pady=5,
                              padx=9)
    destination_label.place(x=40 ,y=120)
 
 
    root.destinationText = Entry(root,
                                 width=27,
                                 textvariable=download_Path,
                                 font="Arial 14")
    root.destinationText.place(x=140 ,y=123)
 
 
    browse_B = Button(root,
                      text="Browse",
                      command=Browse,
                      width=10,
                      bg="bisque",
                      relief=GROOVE)
    browse_B.place(x=455 ,y=124)
 
    Download_B = Button(root,
                        text="Download Video",
                        command=download,
                        width=20,
                        bg="thistle1",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Georgia, 13")
    Download_B.place(x=70 ,y=180)

    Download_C = Button(root,
                        text="Download Audio",
                        command=Download,
                        width=20,
                        bg="thistle1",
                        pady=10,
                        padx=15,
                        relief=GROOVE,
                        font="Georgia, 13")
    Download_C.place(x=310 ,y=180)
    
 
# Defining Browse() to select a
# destination folder to save the video
 
def Browse():

    # Presenting user with a pop-up for
    # directory selection. Retrieving the
    # user-input destination directory and
    # storing it in downloadDirectory
    download_Directory = filedialog.askdirectory(
        initialdir="Your Directory Path", title="Save File")
 
    # Displaying the directory in the directory
    # textbox
    download_Path.set(download_Directory)
 
# Defining Download() to download the audio
 
 
def Download():
    
    # getting user-input Youtube Link
    Youtube_link = video_Link.get()
    download_Folder = download_Path.get()
    getVideo = YouTube(Youtube_link)

    # getting only audio format 
    audioStream = getVideo.streams.get_audio_only()
    audioStream.download(download_Folder)
    
    messagebox.showinfo("Successful!",
                        "Downloaded Audio and saved in\n"
                        + download_Folder)

# Defining download() to download the video

def download():

    Youtube_link = video_Link.get()
    download_Folder = download_Path.get()
    getVideo = YouTube(Youtube_link)

    # getting only highest resolution    
    videoStream = getVideo.streams.get_highest_resolution()
    videoStream.download(download_Folder)

    
 
    # Displaying the message
    messagebox.showinfo("Successful!",
                        "Downloaded Video and saved in\n"
                        + download_Folder)
 
 
# Creating object of tk class
root = tk.Tk()
 
# Setting the title, background color
# and size of the tkinter window and
# disabling the resizing property
root.geometry("600x300")
root.resizable(0, 0)
root.title("YouTube Video Downloader")
root.config(background="#D9D8D7")
 
# Creating the tkinter Variables
video_Link = StringVar()
download_Path = StringVar()
 
# Calling the Widgets() function
Widgets()
 
# Defining infinite loop to run
# application
root.mainloop()