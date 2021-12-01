from tkinter import *
from tkinter import messagebox

win = Tk()
win.geometry("200x100")

def fun():
    messagebox.showinfo("Hello", "Red Button clicked")


b1 = Button(win, text="Red", command=fun, activeforeground="red", activebackground="pink", pady=5, padx=5, state="normal")

b2 = Button(win, text="Blue", activeforeground="blue", activebackground="pink", pady=5, padx=5, relief="ridge")

b3 = Button(win, text="Green", activeforeground="green", activebackground="pink", pady=5, padx=5)

b4 = Button(win, text="Yellow", activeforeground="yellow", activebackground="pink", pady=5, padx=5)

b1.pack(side=LEFT)

b2.pack(side=RIGHT)

b3.pack(side=TOP)

b4.pack(side=BOTTOM)

win.mainloop()
