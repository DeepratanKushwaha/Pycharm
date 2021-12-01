from tkinter import *
from tkinter import messagebox
import math

screen = Tk()
screen.title("My Calculator")
screen.configure(bg="blue")
screen.geometry("362x488")
screen.maxsize(width=453, height=490)
screen.minsize(width=362, height=490)
#screen.iconbitmap("cal.ico")


def click(number):
    global operator
    operator += str(number)
    text.set(operator)


def clear():
    global operator
    operator = ""
    text.set(operator)


def equal():
    global operator
    try:
        result = eval(operator)
        operator = str(result)
        text.set(result)
    except:
        messagebox.showinfo("Notification", "Try again something went wrong")


def Sin():
    global operator
    try:
        result = math.sin(eval(text.get()))
        operator = str(result)
        text.set(operator)
    except:
        messagebox.showinfo("Notification", "Try again something went wrong")


def Cos():
    global operator
    try:
        result = math.cos(eval(text.get()))
        operator = str(result)
        text.set(operator)
    except:
        messagebox.showinfo("Notification", " Try again something went wrong")


def Tan():
    global operator
    try:
        result = math.tan(eval(text.get()))
        operator = str(result)
        text.set(operator)
    except:
        messagebox.showinfo("Notification", " Try again something went wrong")


def Sqrt():
    global operator
    try:
        result = math.sqrt(eval(text.get()))
        operator = str(result)
        text.set(operator)
    except:
        messagebox.showinfo("Notification", " Try again something went wrong")


def Log():
    global operator
    try:
        result = math.log(eval(text.get()))
        operator = str(result)
        text.set(operator)
    except:
        messagebox.showinfo("Notification", " Try again something went wrong")


# ===================Binding function=================
def on_enter7(event):
    btn7.configure(bg="red")


def on_leave7(event):
    btn7.configure(bg="powder blue")


def on_enter8(event):
    btn8.configure(bg="red")


def on_leave8(event):
    btn8.configure(bg="powder blue")


def on_enter9(event):
    btn9.configure(bg="red")


def on_leave9(event):
    btn9.configure(bg="powder blue")


def on_enterAdd(event):
    btnAdd.configure(bg="red")


def on_leaveAdd(event):
    btnAdd.configure(bg="powder blue")


def on_enter4(event):
    btn4.configure(bg="red")


def on_leave4(event):
    btn4.configure(bg="powder blue")


def on_enter5(event):
    btn5.configure(bg="red")


def on_leave5(event):
    btn5.configure(bg="powder blue")


def on_enter6(event):
    btn6.configure(bg="red")


def on_leave6(event):
    btn6.configure(bg="powder blue")


def on_enterSub(event):
    btnSub.configure(bg="red")


def on_leaveSub(event):
    btnSub.configure(bg="powder blue")


def on_enter1(event):
    btn1.configure(bg="red")


def on_leave1(event):
    btn1.configure(bg="powder blue")


def on_enter2(event):
    btn2.configure(bg="red")


def on_leave2(event):
    btn2.configure(bg="powder blue")


def on_enter3(event):
    btn3.configure(bg="red")


def on_leave3(event):
    btn3.configure(bg="powder blue")


def on_enterMul(event):
    btnMul.configure(bg="red")


def on_leaveMul(event):
    btnMul.configure(bg="powder blue")


def on_enter0(event):
    btn0.configure(bg="red")


def on_leave0(event):
    btn0.configure(bg="powder blue")


def on_enterClear(event):
    btnClear.configure(bg="red")


def on_leaveClear(event):
    btnClear.configure(bg="powder blue")


def on_enterEqual(event):
    btnEqual.configure(bg="red")


def on_leaveEqual(event):
    btnEqual.configure(bg="powder blue")


def on_enterDiv(event):
    btnDiv.configure(bg="red")


def on_leaveDiv(event):
    btnDiv.configure(bg="powder blue")


def on_entryEnter(event):
    entry1.configure(bg="red")


def on_entryLeave(event):
    entry1.configure(bg="powder blue")


def on_enterSin(event):
    btnSin.configure(bg="red")


def on_leaveSin(event):
    btnSin.configure(bg="powder blue")


def on_enterCos(event):
    btnCos.configure(bg="red")


def on_leaveCos(event):
    btnCos.configure(bg="powder blue")


def on_enterTan(event):
    btnTan.configure(bg="red")


def on_leaveTan(event):
    btnTan.configure(bg="powder blue")


def on_enterSqrt(event):
    btnSqrt.configure(bg="red")


def on_leaveSqrt(event):
    btnSqrt.configure(bg="powder blue")


def on_enterLog(event):
    btnLog.configure(bg="red")


def on_leaveLog(event):
    btnLog.configure(bg="powder blue")


text = StringVar()
operator = ""

entry1 = Entry(screen, bg="orange", font="arial 20 italic bold", bd=30, justify="right", textvariable=text)
entry1.grid(row=0, columnspan=4)
entry1.bind("<Enter>", on_entryEnter)
entry1.bind("<Leave>", on_entryLeave)

btn7 = Button(screen, text="7", font="arial 20 italic bold", bd=8, padx=16, pady=16, command=lambda: click(7),
              activebackground="green", activeforeground="white", bg="powder blue")
btn7.grid(row=1, column=0)
btn7.bind("<Enter>", on_enter7)
btn7.bind("<Leave>", on_leave7)

btn8 = Button(screen, text="8", font="arial 20 italic bold", bd=8, padx=16, pady=16, command=lambda: click(8),
              activebackground="green", activeforeground="white", bg="powder blue")
btn8.grid(row=1, column=1)
btn8.bind("<Enter>", on_enter8)
btn8.bind("<Leave>", on_leave8)

btn9 = Button(screen, text="9", font="arial 20 italic bold", bd=8, padx=16, pady=16, command=lambda: click(9),
              activebackground="green", activeforeground="white", bg="powder blue")
btn9.grid(row=1, column=2)
btn9.bind("<Enter>", on_enter9)
btn9.bind("<Leave>", on_leave9)

btnAdd = Button(screen, text="+", font="arial 20 italic bold", bd=8, padx=16, pady=16, command=lambda: click("+"),
                activebackground="green", activeforeground="white", bg="powder blue")
btnAdd.grid(row=1, column=3)
btnAdd.bind("<Enter>", on_enterAdd)
btnAdd.bind("<Leave>", on_leaveAdd)

btn4 = Button(screen, text="4", font="arial 20 italic bold", bd=8, padx=16, pady=16, command=lambda: click(4),
              activebackground="green", activeforeground="white", bg="powder blue")
btn4.grid(row=2, column=0)
btn4.bind("<Enter>", on_enter4)
btn4.bind("<Leave>", on_leave4)

btn5 = Button(screen, text="5", font="arial 20 italic bold", bd=8, padx=16, pady=16, command=lambda: click(5),
              activebackground="green", activeforeground="white", bg="powder blue")
btn5.grid(row=2, column=1)
btn5.bind("<Enter>", on_enter5)
btn5.bind("<Leave>", on_leave5)

btn6 = Button(screen, text="6", font="arial 20 italic bold", bd=8, padx=16, pady=16, command=lambda: click(6),
              activebackground="green", activeforeground="white", bg="powder blue")
btn6.grid(row=2, column=2)
btn6.bind("<Enter>", on_enter6)
btn6.bind("<Leave>", on_leave6)

btnSub = Button(screen, text="-", font="arial 20 italic bold", bd=8, padx=19, pady=16, command=lambda: click("-"),
                activebackground="green", activeforeground="white", bg="powder blue")
btnSub.grid(row=2, column=3)
btnSub.bind("<Enter>", on_enterSub)
btnSub.bind("<Leave>", on_leaveSub)

btn1 = Button(screen, text="1", font="arial 20 italic bold", bd=8, padx=16, pady=16, command=lambda: click(1),
              activebackground="green", activeforeground="white", bg="powder blue")
btn1.grid(row=3, column=0)
btn1.bind("<Enter>", on_enter1)
btn1.bind("<Leave>", on_leave1)

btn2 = Button(screen, text="2", font="arial 20 italic bold", bd=8, padx=16, pady=16, command=lambda: click(2),
              activebackground="green", activeforeground="white", bg="powder blue")
btn2.grid(row=3, column=1)
btn2.bind("<Enter>", on_enter2)
btn2.bind("<Leave>", on_leave2)

btn3 = Button(screen, text="3", font="arial 20 italic bold", bd=8, padx=16, pady=16, command=lambda: click(3),
              activebackground="green", activeforeground="white", bg="powder blue")
btn3.grid(row=3, column=2)
btn3.bind("<Enter>", on_enter3)
btn3.bind("<Leave>", on_leave3)

btnMul = Button(screen, text="*", font="arial 20 italic bold", bd=8, padx=18, pady=16, command=lambda: click("*"),
                activebackground="green", activeforeground="white", bg="powder blue")
btnMul.grid(row=3, column=3)
btnMul.bind("<Enter>", on_enterMul)
btnMul.bind("<Leave>", on_leaveMul)

btn0 = Button(screen, text="0", font="arial 20 italic bold", bd=8, padx=16, pady=16, command=lambda: click(0),
              activebackground="green", activeforeground="white", bg="powder blue")
btn0.grid(row=4, column=0)
btn0.bind("<Enter>", on_enter0)
btn0.bind("<Leave>", on_leave0)

btnClear = Button(screen, text="C", font="arial 20 italic bold", bd=8, padx=16, pady=16, command=clear,
                  activebackground="green", activeforeground="white", bg="powder blue")
btnClear.grid(row=4, column=1)
btnClear.bind("<Enter>", on_enterClear)
btnClear.bind("<Leave>", on_leaveClear)

btnEqual = Button(screen, text="=", font="arial 20 italic bold", bd=8, padx=16, pady=16, command=equal,
                  activebackground="green", activeforeground="white", bg="powder blue")
btnEqual.grid(row=4, column=2)
btnEqual.bind("<Enter>", on_enterEqual)
btnEqual.bind("<Leave>", on_leaveEqual)

btnDiv = Button(screen, text="/", font="arial 20 italic bold", bd=8, padx=19, pady=16, command=lambda: click("/"),
                activebackground="green", activeforeground="white", bg="powder blue")
btnDiv.grid(row=4, column=3)
btnDiv.bind("<Enter>", on_enterDiv)
btnDiv.bind("<Leave>", on_leaveDiv)

# ==================================Scientific Functions================================

btnSin = Button(screen, text="sin", font="arial 15 italic bold", bd=8, padx=14, pady=21, command=Sin,
                activebackground="green", activeforeground="white", bg="powder blue")
btnSin.grid(row=0, column=4)
btnSin.bind("<Enter>", on_enterSin)
btnSin.bind("<Leave>", on_leaveSin)

btnCos = Button(screen, text="cos", font="arial 15 italic bold", bd=8, padx=12, pady=23, command=Cos,
                activebackground="green", activeforeground="white", bg="powder blue")
btnCos.grid(row=1, column=4)
btnCos.bind("<Enter>", on_enterCos)
btnCos.bind("<Leave>", on_leaveCos)

btnTan = Button(screen, text="tan", font="arial 15 italic bold", bd=8, padx=14, pady=23, command=Tan,
                activebackground="green", activeforeground="white", bg="powder blue")
btnTan.grid(row=2, column=4)
btnTan.bind("<Enter>", on_enterTan)
btnTan.bind("<Leave>", on_leaveTan)

btnSqrt = Button(screen, text="sqrt", font="arial 15 italic bold", bd=8, padx=12, pady=23, command=Sqrt,
                 activebackground="green", activeforeground="white", bg="powder blue")
btnSqrt.grid(row=3, column=4)
btnSqrt.bind("<Enter>", on_enterSqrt)
btnSqrt.bind("<Leave>", on_leaveSqrt)

btnLog = Button(screen, text="log", font="arial 15 italic bold", bd=8, padx=14, pady=23, command=Log,
                activebackground="green", activeforeground="white", bg="powder blue")
btnLog.grid(row=4, column=4)
btnLog.bind("<Enter>", on_enterLog)
btnLog.bind("<Leave>", on_leaveLog)

screen.mainloop()
