from tkinter import *

root = Tk()
def go():

cl = "\u2667"

for x in range(1, 200):
        button1['text'] = cl
        button1['font'] = ("", x)
        root.update_idletasks()
        root.title("happy")


button1 = Button(root, text='GO', fg='green', command=go)
button1.pack()

root.mainloop()
