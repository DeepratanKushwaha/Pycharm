from tkinter import *
from pytube import YouTube

root = Tk()
root.title("YouTube Video Downloader")
root.geometry('500x500+400+100')
root.resizable(0, 0)


def download():
    try:
        myVar.set('Downloading...')
        root.update()
        YouTube(linkVar.get()).streams.first().download()
        linkVar.set('Video Downloaded Successfully')
    except EXCEPTION as e:
        myVar.set('Error')
        root.update()
        linkVar.set('Enter correct link\nOr check your internet connection')
        print(e)


label1 = Label(root, text='Welcome to youtube\nDownloader application', font='Consolas 15 bold')
label1.pack()

myVar = StringVar()
entry1 = Entry(root, textvariable=myVar, width=50)
myVar.set('Enter the link below')
entry1.pack(pady=10)

linkVar = StringVar()
entry2 = Entry(root, textvariable=linkVar, width=50)
entry2.pack(pady=10)

button = Button(root, text='Download Video', command=download)
button.pack()

root.mainloop()
