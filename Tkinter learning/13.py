from tkinter import *


def resize():
    new_width = width.get()
    new_height = height.get()
    root.geometry(f"{new_width}x{new_height}")


root = Tk()
root.geometry("300x300")

l1 = Label(root, text="Width", font="comicsansms 10 bold").grid(row=1, column=1)
l2 = Label(root, text="Height", font="comicsansms 10 bold").grid(row=2, column=1)

width = StringVar()
height = StringVar()

width_entry = Entry(root, textvariable=width).grid(row=1, column=2)
height_entry = Entry(root, textvariable=height).grid(row=2, column=2)

b1 = Button(root, text="Apply", command=resize, font="comicsansms 10 bold").grid(row=3, column=1)


root.mainloop()