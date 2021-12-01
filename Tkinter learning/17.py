from tkinter import *
import tkinter.messagebox as msg

root = Tk()
root.geometry("500x400")
root.title("Radio Button")


def order():
    msg.showinfo("order received", f"we have received your order for {var.get()}. Thanks for ordering")


# var = IntVar()
var = StringVar()
var.set("Radio")

Label(root, text="What would you like to have sir?", font="lucida 15 bold", justify=LEFT, padx=12).pack()
radio = Radiobutton(root, text="Dosa", padx=14, variable=var, value="Dosa").pack(anchor=W)
radio = Radiobutton(root, text="Idli", padx=14, variable=var, value="Idli").pack(anchor=W)
radio = Radiobutton(root, text="Fritters", padx=14, variable=var, value="Fritters").pack(anchor=W)
radio = Radiobutton(root, text="Rissole", padx=14, variable=var, value="Rissole").pack(anchor=W)

Button(root, text="order now", command=order).pack()

root.mainloop()
