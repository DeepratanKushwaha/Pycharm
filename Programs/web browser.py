
import tkinter as tk
from tkinter import *
import webbrowser

win = tk.Tk()
win.title("WebBrowser")
win.geometry("300x300")
win.iconbitmap('C:/Users/mss2015/Desktop/wallpaper/google-logo.png')


def google():
    webbrowser.open("www.google.com")


def youtube():
    webbrowser.open("www.youtube.com")


def amazon():
    webbrowser.open("www.amazon.com")


def facebook():
    webbrowser.open("www.facebook.com")


igoogle = PhotoImage(file="C:/Users/mss2015/Desktop/wallpaper/google-logo.png")
google = tk.Button(win, image=igoogle, command=google)
google.grid(row=0, column=0)

iyoutube = PhotoImage(file="C:/Users/mss2015/Desktop/wallpaper/youtube.png")
youtube = tk.Button(win, image=iyoutube, command=youtube)
youtube.grid(row=0, column=1)

iamazon = PhotoImage(file="C:/Users/mss2015/Desktop/wallpaper/download.png")
amazon = tk.Button(win, image=iamazon, command=amazon)
amazon.grid(row=0, column=2)

ifacebook = PhotoImage(file="C:/Users/mss2015/Desktop/wallpaper/facebook-new.png")
facebook = tk.Button(win, image=ifacebook, command=facebook)
facebook.grid(row=0, column=3)

win.mainloop()
