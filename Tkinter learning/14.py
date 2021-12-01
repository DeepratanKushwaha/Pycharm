from tkinter import *


def myFunc():
    print("Success")


root = Tk()
root.geometry("500x400")
root.title("Pycharm")

# non dropdown menu
# mymenu = Menu(root)
# mymenu.add_command(label="File")
# mymenu.add_command(label="Exit")

# root.config(menu=mymenu)

mainMenu = Menu(root)
m1 = Menu(mainMenu, tearoff=0)
m1.add_command(label="New", command=myFunc)
m1.add_command(label="Open", command=myFunc)
m1.add_command(label="Save", command=myFunc)
m1.add_command(label="Quit", command=myFunc)
root.config(menu=mainMenu)

mainMenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainMenu, tearoff=0)
m2.add_command(label="Undo", command=myFunc)
m2.add_command(label="Redo", command=myFunc)
m2.add_command(label="Cut", command=myFunc)
m2.add_command(label="Paste", command=myFunc)
root.config(menu=mainMenu)

mainMenu.add_cascade(label="Edit", menu=m2)


root.mainloop()
