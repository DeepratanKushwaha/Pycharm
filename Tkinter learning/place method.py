from tkinter import *

win = Tk()
win.geometry("400x250")

name = Label(win, text="Name").place(x=30, y=50)
email = Label(win, text="Email").place(x=30, y=90)
password = Label(win, text="Password").place(x=30, y=130)

e1 = Entry(win).place(x=80, y=50)
e2 = Entry(win).place(x=80, y=90)
e3 = Entry(win).place(x=95, y=130)

win.mainloop()
