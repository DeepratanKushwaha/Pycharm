from tkinter import *


def getvals():
    print(f"The value of username is {uservalue.get()}")
    print(f"The value of password is {passvalue.get()}")


root = Tk()
root.geometry("655x333")

user = Label(root, text="UserName", borderwidth=3, relief=RIDGE)
user.grid()

Password = Label(root, text="Password", borderwidth=3, relief=RIDGE)
Password.grid(row=1)

# classes in tkinter
# BooleanVar, DoubleVar, IntVar, StringVar

uservalue = StringVar()
passvalue = StringVar()

userentry = Entry(root, textvariable=uservalue).grid(row=0, column=1, padx=20)
passentry = Entry(root, textvariable=passvalue).grid(row=1, column=1, padx=20)

b1 = Button(text="Submit", command=getvals).grid()


root.mainloop()
