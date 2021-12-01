from tkinter import *


def btnClick(numbers):
    global operator
    operator = operator + str(numbers)
    textInput.set(operator)


def btnClear():
    global operator
    operator = ""
    textInput.set("")           # we can also use operator instead of ""


def btnEqual():
    global operator
    sumUp = str(eval(operator))
    textInput.set(sumUp)
    operator = ""


cal = Tk()
cal.title("Calculator")
operator = ""

textInput = StringVar()
textDisplay = Entry(cal, textvariable=textInput, font="arial 20 bold", bd=30, insertwidth=4, bg="powder blue",
                    justify=RIGHT).grid(columnspan=4)

b7 = Button(cal, text="7", font="arial 20 bold", fg="black", bd=8, padx=16, pady=16,
            bg="powder blue", command=lambda: btnClick(7)).grid(row=1, column=0)
b8 = Button(cal, text="8", font="arial 20 bold", fg="black", bd=8, padx=16, pady=16,
            bg="powder blue", command=lambda: btnClick(8)).grid(row=1, column=1)
b9 = Button(cal, text="9", font="arial 20 bold", fg="black", bd=8, padx=16, pady=16,
            bg="powder blue", command=lambda: btnClick(9)).grid(row=1, column=2)
addition = Button(cal, text="+", font="arial 20 bold", fg="black", bd=8, padx=16, pady=16,
                  bg="powder blue", command=lambda: btnClick("+")).grid(row=1, column=3)

b4 = Button(cal, text="4", font="arial 20 bold", fg="black", bd=8, padx=16, pady=16,
            bg="powder blue", command=lambda: btnClick(4)).grid(row=2, column=0)
b5 = Button(cal, text="5", font="arial 20 bold", fg="black", bd=8, padx=16, pady=16,
            bg="powder blue", command=lambda: btnClick(5)).grid(row=2, column=1)
b6 = Button(cal, text="6", font="arial 20 bold", fg="black", bd=8, padx=16, pady=16,
            bg="powder blue", command=lambda: btnClick(6)).grid(row=2, column=2)
subtraction = Button(cal, text="-", font="arial 20 bold", fg="black", bd=8, padx=16, pady=16,
                     bg="powder blue", command=lambda: btnClick("-")).grid(row=2, column=3)

b1 = Button(cal, text="1", font="arial 20 bold", fg="black", bd=8, padx=16, pady=16,
            bg="powder blue", command=lambda: btnClick(1)).grid(row=3, column=0)
b2 = Button(cal, text="2", font="arial 20 bold", fg="black", bd=8, padx=16, pady=16,
            bg="powder blue", command=lambda: btnClick(2)).grid(row=3, column=1)
b3 = Button(cal, text="3", font="arial 20 bold", fg="black", bd=8, padx=16, pady=16,
            bg="powder blue", command=lambda: btnClick(3)).grid(row=3, column=2)
multiply = Button(cal, text="*", font="arial 20 bold", fg="black", bd=8, padx=16, pady=16,
                  bg="powder blue", command=lambda: btnClick("*")).grid(row=3, column=3)

b0 = Button(cal, text="7", font="arial 20 bold", fg="black", bd=8, padx=16, pady=16,
            bg="powder blue", command=lambda: btnClick(0)).grid(row=4, column=0)
clear = Button(cal, text="C", font="arial 20 bold", fg="black", bd=8, padx=16, pady=16,
               bg="powder blue", command=btnClear).grid(row=4, column=1)
equal = Button(cal, text="=", font="arial 20 bold", fg="black", bd=8, padx=16, pady=16,
               bg="powder blue", command=btnEqual).grid(row=4, column=2)
division = Button(cal, text="/", font="arial 20 bold", fg="black", bd=8, padx=16, pady=16,
                  bg="powder blue", command=lambda: btnClick("/")).grid(row=4, column=3)


cal.mainloop()
