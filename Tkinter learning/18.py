from tkinter import *

root = Tk()
root.geometry("500x400")
root.title("ListBox")

i = 0


def add():
    global i
    ls1.insert(ACTIVE, f"{i}")
    i += 1
    

ls1 = Listbox(root)
ls1.pack()
ls1.insert(END, "First item of our listbox")

Button(root, text="Add Item", command=add).pack()

root.mainloop()
