from tkinter import *
import tkinter.messagebox as msg


def myFunc():
    print("Success")


def help():
    print("im here")
    msg.showinfo("Help", "i will help you")


def rate():
    print("Rate us")
    value = msg.askquestion("was your experience good?", "you used this gui... Was your experience good?")
    print(value)
    if value == "yes":
        msgs = "Great. Rate us on play store"
    else:
        msgs = "tell us what went wrong. we will call you"
    msg.showinfo("Experience", msgs)


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
m1.add_separator()
m1.add_command(label="Save", command=myFunc)
m1.add_command(label="Quit", command=myFunc)
root.config(menu=mainMenu)

mainMenu.add_cascade(label="File", menu=m1)

m2 = Menu(mainMenu, tearoff=0)
m2.add_command(label="Undo", command=myFunc)
m2.add_command(label="Redo", command=myFunc)
m2.add_separator()
m2.add_command(label="Cut", command=myFunc)
m2.add_command(label="Paste", command=myFunc)
root.config(menu=mainMenu)

mainMenu.add_cascade(label="Edit", menu=m2)

m3 = Menu(mainMenu, tearoff=0)
m3.add_command(label="Help", command=help)
m3.add_command(label="Rate us", command=rate)
root.config(menu=mainMenu)

mainMenu.add_cascade(label="Help", menu=m3)

root.mainloop()
