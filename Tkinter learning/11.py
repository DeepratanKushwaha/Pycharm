from tkinter import *


def deep(event):
    print(f"you clicked on button at {event.x}, {event.y}")


root = Tk()
root.title("Events in Tkinter")
root.geometry("400x200")

widget = Button(root, text="Click button")
widget.pack()

widget.bind('<Button-1>', deep)
widget.bind('<Double-1>', quit)

root.mainloop()