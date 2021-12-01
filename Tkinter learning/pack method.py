from tkinter import *

win = Tk()
redbutton = Button(win, text="Red", fg="red")
redbutton.pack(side=LEFT)

greenbutton = Button(win, text="Green", fg="green")
greenbutton.pack(side=RIGHT)

bluebutton = Button(win, text="Blue", fg="blue")
bluebutton.pack(side=TOP)

blackbutton = Button(win, text="Black", fg="black")
blackbutton.pack(side=BOTTOM)

win.mainloop()