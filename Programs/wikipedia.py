
import wikipedia
import tkinter as tk
from tkinter import *
from tkinter.messagebox import showinfo

win = tk.Tk()
win.title("Wikipedia")
win.geometry("300x100")


def search_wiki():
    search = entry.get()


answer = wikipedia.summary(search_wiki())
showinfo("Wikipedia Answer", answer)


# Creating label
label = Label(win, text="Wikipedia Search :")
label.grid(row=0, column=0)

# Creating Entry box
entry = Entry(win)
entry.grid(row=1, column=0)

# Creating Button
button = Button(win, text="Search", command=search_wiki)
button.grid(row=1, column=1, padx=10)

win.mainloop()
