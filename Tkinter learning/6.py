from tkinter import *

root = Tk()
root.geometry("655x333")


def Hello():
    print("hello")


f1 = Frame(root, borderwidth=6, bg="grey", relief=SUNKEN)
f1.pack(side=LEFT, anchor="nw")

b1 = Button(f1, fg="red", text="Print Now", command=Hello)
b1.pack(side=LEFT, padx=20)

b2 = Button(f1, fg="red", text="Print Now")
b2.pack(side=LEFT, padx=20)

b3 = Button(f1, fg="red", text="Print Now")
b3.pack(side=LEFT, padx=20)

b4 = Button(f1, fg="red", text="Print Now")
b4.pack(side=LEFT, padx=20)
root.mainloop()
