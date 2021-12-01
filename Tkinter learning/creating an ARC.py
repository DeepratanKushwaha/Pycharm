from tkinter import *

win = Tk()
win.geometry("200x200")

# creating an simple arc

c = Canvas(win, bg="black", height="200", width="200")
c.create_arc((5, 10, 150, 200), start=0, extent=150, fill="white")

c.pack()

win.mainloop()
