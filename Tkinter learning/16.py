from tkinter import *
import tkinter.messagebox as msg
root = Tk()
root.geometry("500x400")
root.title("Sliders")


def getMoney():
    print(f"we have credited {myslider1.get()} rupees to your bank account")
    msg.showinfo("Amount Credited", f"we have credited {myslider1.get()} rupees to your bank account")

# myslider = Scale(root, from_=0, to=400)
# myslider.pack()


Label(root, text="how much money you want").pack()
myslider1 = Scale(root, from_=0, to=400, orient=HORIZONTAL, tickinterval=200)
myslider1.set(200)
myslider1.pack()
Button(root, text="Get money", command=getMoney).pack(pady=10)


root.mainloop()
