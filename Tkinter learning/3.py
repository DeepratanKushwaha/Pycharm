from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry('800x500')
# photo = PhotoImage(file="png file")

# for jpg images

image = Image.open("1.jpg")
photo = ImageTk.PhotoImage(image)

deep_image = Label(image=photo)
deep_image.pack()

root.mainloop()