from tkinter import *

root = Tk()

# width x height
root.geometry("400x300")

# width, height
root.minsize(200, 100)

# width, height
root.maxsize(500, 300)

l1 = Label(text="Deep")
l1.pack()


root.mainloop()
