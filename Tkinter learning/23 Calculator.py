from tkinter import *


def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                value = "Error"
                print(e)

        scvalue.set(value)
        screen.update()

    elif text == "c":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()


root = Tk()
root.geometry("200x466")
root.title("Calculator")
# root.configure(bg="")
scvalue = StringVar()

screen = Entry(root, textvar=scvalue, font="lucida 40 ")
screen.pack(fill=X, pady=10)

f1 = Frame(root, bg="powder blue")
b = Button(f1, text="9", padx=10, pady=5, font="comicsansms 10 bold", relief=GROOVE, borderwidth=10, fg="red",
           bg="violet")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)
b = Button(f1, text="8", padx=10, pady=5, font="comicsansms 10 bold", relief=GROOVE, borderwidth=10, fg="blue",
           bg="violet")
b.pack(side=LEFT, padx=1, pady=5)
b.bind("<Button-1>", click)
b = Button(f1, text="7", padx=10, pady=5, font="comicsansms 10 bold", relief=GROOVE, borderwidth=10, fg="green",
           bg="violet")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)
f1.pack()

f1 = Frame(root, bg="cyan")
b = Button(f1, text="6", padx=10, pady=5, font="comicsansms 10 bold", relief=GROOVE, borderwidth=10, fg="red",
           bg="violet")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)
b = Button(f1, text="5", padx=10, pady=5, font="comicsansms 10 bold", relief=GROOVE, borderwidth=10, fg="blue",
           bg="violet")
b.pack(side=LEFT, padx=1, pady=5)
b.bind("<Button-1>", click)
b = Button(f1, text="4", padx=10, pady=5, font="comicsansms 10 bold", relief=GROOVE, borderwidth=10, fg="green",
           bg="violet")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)
f1.pack()

f1 = Frame(root, bg="cyan")
b = Button(f1, text="3", padx=10, pady=5, font="comicsansms 10 bold", relief=GROOVE, borderwidth=10, fg="red",
           bg="violet")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)
b = Button(f1, text="2", padx=10, pady=5, font="comicsansms 10 bold", relief=GROOVE, borderwidth=10, fg="blue",
           bg="violet")
b.pack(side=LEFT, padx=1, pady=5)
b.bind("<Button-1>", click)
b = Button(f1, text="1", padx=10, pady=5, font="comicsansms 10 bold", relief=GROOVE, borderwidth=10, fg="green",
           bg="violet")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)
f1.pack()

f1 = Frame(root, bg="cyan")
b = Button(f1, text="0", padx=10, pady=5, font="comicsansms 10 bold", relief=GROOVE, borderwidth=10, fg="red",
           bg="violet")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)
b = Button(f1, text="=", padx=10, pady=5, font="comicsansms 10 bold", relief=GROOVE, borderwidth=10, fg="blue",
           bg="violet")
b.pack(side=LEFT, padx=1, pady=5)
b.bind("<Button-1>", click)
b = Button(f1, text="c", padx=10, pady=5, font="comicsansms 10 bold", relief=GROOVE, borderwidth=10, fg="green",
           bg="violet")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)
f1.pack()

f1 = Frame(root, bg="cyan")
b = Button(f1, text="+", padx=10, pady=5, font="comicsansms 10 bold", relief=GROOVE, borderwidth=10, fg="red",
           bg="violet")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)
b = Button(f1, text="-", padx=12, pady=5, font="comicsansms 10 bold", relief=GROOVE, borderwidth=10, fg="blue",
           bg="violet")
b.pack(side=LEFT, padx=1, pady=5)
b.bind("<Button-1>", click)
b = Button(f1, text="*", padx=10, pady=5, font="comicsansms 10 bold", relief=GROOVE, borderwidth=10, fg="green",
           bg="violet")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)
f1.pack()

f1 = Frame(root, bg="cyan")
b = Button(f1, text="/", padx=12, pady=5, font="comicsansms 10 bold", relief=GROOVE, borderwidth=10, fg="red",
           bg="violet")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)
b = Button(f1, text="%", padx=9, pady=5, font="comicsansms 10 bold", relief=GROOVE, borderwidth=10, fg="blue",
           bg="violet")
b.pack(side=LEFT, padx=1, pady=5)
b.bind("<Button-1>", click)
b = Button(f1, text=".", padx=10, pady=5, font="comicsansms 10 bold", relief=GROOVE, borderwidth=10, fg="green",
           bg="violet")
b.pack(side=LEFT, padx=5, pady=3)
b.bind("<Button-1>", click)
f1.pack()


root.mainloop()
