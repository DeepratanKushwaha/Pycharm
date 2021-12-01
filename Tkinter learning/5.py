from tkinter import *

root = Tk()
root.geometry("655x333")
f1 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f1.pack(side=LEFT, fill=Y)

f2 = Frame(root, bg="grey", borderwidth=6, relief=SUNKEN)
f2.pack(side=TOP, fill=X)

l1 = Label(f1, text="Project Tkinter")
l1.pack(padx=30, pady=30)

l2 = Label(f2, text="Sublime Text", font="helvetica 15 bold", fg="red")
l2.pack()

root.mainloop()
