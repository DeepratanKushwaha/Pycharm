import youtube_dl
import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog

# Creating object of tk class
root = tk.Tk()

# setting the title, background color and size of the tkinter window and disabling the
# resizing property
root.geometry("500x120")
root.resizable(TRUE, TRUE)
root.title("Py_Youtube_Audio_Downloader")
root.config(background="turquoise4")

# creating the tkinter variables
videoLink = StringVar()
downloadPath = StringVar()


def CreateWidgets():
    linkLable = Label(root, text="YOUTUBE LINK :", bg="turquoise4")
    linkLable.grid(row=1, column=1, pady=5, padx=5)

    rootlinkText = Entry(root, width=55, textvariable=videoLink)
    rootlinkText.grid(row=2, column=0, pady=5, padx=5, columnsapn=2)

    destinationLabel = Label(root, text="DESTINATION :", bg="turquiose4")
    destinationLabel.grid(row=2, column=0, pady=5, padx=5)

    root.destinationText = Entry(root, width=38, textvariable=downloadPath)
    root.destinationText.grid(row=2, column=1, pady=5, padyx=5)

    def Browser():
        dwldDirectory = filedialog.askdirectory(initialdir="/Users/mss2015/Downloads")

        downloadPath.set(dwldDirectory)

        browsebutton = Button(root, text="BROWSE", command=Browser, width=15)
        browsebutton.grid(row=3, column=1, pady=5, padyx=5)


def Download():
    yt_link = videoLink.get()

    dwldFolder = downloadPath.get()

    audDWLDopt = {

        'format': 'bestaudio/best',

        'outtmpl': dwldFolder + "/%(title)s.%(ext)s",

        'postprocessors': [{

            'key': 'FFmpegExtractAudio',

            'perferredcodec': 'mp3',

            'preferredquality': '320'
        }],
    }

    with youtube_dl.YoutubeDL(audDWLDopt) as aud_dlwd:
        aud_dlwd.download(yt_link)

    # displaying the message

    messagebox.showinfo("SUCCESS", "VIDEO CONVERTED AND DOWNLOADED AS AUDIO")


# Calling the CreateWidgets() function
CreateWidgets()

# defining infinite loop to run application
root.mainloop()
