from tkinter import *
import os

win = Tk()
win.title("Shutdown And Restart")
win.geometry("270x60")


def shutdown():
    os.system("shutdown /r /t 1")


def restart():
    os.system("shutdown /r /t 1")


button1 = Button(win, text="Shutdown", command=shutdown, height=3, width=17)
button1.grid(row=0, column=0)

button2 = Button(win, text="Restart", command=restart, height=3, width=17)
button2.grid(row=0, column=1)

win.mainloop()
