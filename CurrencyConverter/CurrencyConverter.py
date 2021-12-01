from tkinter import *
from PIL import ImageTk
from tkinter import font
from tkinter import messagebox
from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter

root = Tk()
root.title('Currency Converter')
root.minsize(600, 500)
root.maxsize(600, 500)
HEIGHT = 500
WIDTH = 500
FONT = font.Font(family='Comic Sans MS', size="9", weight="bold")


def convert(c1, c2, amount):
    try:
        if amount == '':
            messagebox.showerror('Error', 'Amount not specified')
        elif c1 == 'Select' or c2 == 'Select':
            messagebox.showerror('Error', 'Currency not selected')
        else:
            try:
                amount = float(amount)
                b = BtcConverter()
                c = CurrencyRates()
                if c1 == c2:
                    result = amount
                elif c1 == 'BTC':
                    result = b.convert_btc_to_cur(amount, c2)
                elif c2 == 'BTC':
                    result = b.convert_to_btc(amount, c1)
                else:
                    result = c.convert(c1, c2, int(amount))
                label_down['text'] = f'Conversion Result: \n{amount} {c1} = {result} {c2}'
            except ValueError:
                messagebox.showerror('Error', 'Invalid Amount')
                clear()
    except EXCEPTION:
        messagebox.showerror('Error', 'Something went wrong. Please try again')


def clear():
    entry.delete(0, END)
    label_down.configure(text='')


def Help():
    new_root = Tk()
    new_root.title('Reference')
    new_root.minsize(400, 300)
    new_root.maxsize(400, 300)

    new_canvas = Canvas(new_root, height=400, width=300)
    new_canvas.pack()

    new_frame = Frame(new_root, bg='yellow')
    new_frame.place(relwidth=1, relheight=1)

    new_label = Label(new_frame, font='ComicSansMS 12 bold', fg='#001a4d', anchor=NW, justify=LEFT, bd=4)
    new_label.place(relx=0.05, rely=0.05, relwidth=0.89, relheight=0.90)

    new_label['text'] = "Abbreviations:\nBTC - Bitcoin\nUSD - USD Dollar\nEUR - Euro\nJPY - Japanese Yen\nGBP - Pound "\
                        "Sterling\nAUD - Australian Dollar\nCAD - Canadian Dollar\nCHF - Swiss Frank\nINR - Indian " \
                        "Rupees\nRUB - Russian Rubble\nCNY - Chinese Yuan "

    new_button = Button(new_frame, text='Back', font=FONT, bg='pink', fg='black', activeforeground='pink',
                        activebackground='black', command=lambda: new_root.destroy())
    new_button.place(relx=0.76, rely=0.82, relwidth=0.14, relheight=0.11)

    new_root.mainloop()


def Exit():
    root.destroy()


canvas = Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = ImageTk.PhotoImage(file='img.jpeg')
background_label = Label(root, image=background_image)
background_label.place(relwidth=1, relheight=2)

upper_frame = Frame(root, bg='yellow', bd=5)
upper_frame.place(relx=0.5, rely=0.1, relwidth=0.80, relheight=0.25, anchor="n")

label_up = Label(upper_frame)
label_up.place(relwidth=1, relheight=1)

lower_frame = Frame(root, bg='yellow', bd=10)
lower_frame.place(relx=0.5, rely=0.53, relwidth=0.8, relheight=0.25, anchor='n')

label_down = Label(lower_frame, font=FONT, fg="#001a4d", anchor="nw", justify="left", bd=4)
label_down.place(relwidth=1, relheight=1)

label1 = Label(upper_frame, text='From', font=FONT, bd=5, bg='#d9138a', highlightbackground='#d9138a', fg='white')
label1.place(relx=0.15, rely=0.02, relwidth=0.15, relheight=0.25)

label2 = Label(upper_frame, text='To', font=FONT, bd=5, bg='#d9138a', highlightbackground='#d9138a', fg='white')
label2.place(relx=0.7, rely=0.02, relwidth=0.15, relheight=0.25)

# option menu
option = ["BTC", "USD", "EUR", "JPY", "GBP", "AUD", "CAD", "CHF", "INR", "RUB", "CNY"]

clicked1 = StringVar()
clicked1.set('Select')

listbox1 = OptionMenu(upper_frame, clicked1, *option)
listbox1.config(bg='#fc034e', fg='black', activeforeground='#fc034e', activebackground='black', font=FONT, width=15)
listbox1.place(relx=0.07, rely=0.3)

clicked2 = StringVar()
clicked2.set('Select')
listbox2 = OptionMenu(upper_frame, clicked2, *option)
listbox2.config(bg='#fc034e', fg='black', activeforeground='#fc034e', activebackground='black', font=FONT, width=15)
listbox2.place(relx=0.61, rely=0.3)

# logo image between to option list
img = PhotoImage(file='logo.png')
img1 = img.subsample(10, 10)
image_label = Label(upper_frame, image=img1)
image_label.place(relx=0.445, rely=0.2)

# amount
label3 = Label(upper_frame, text='Amount', font=FONT, bg='#12a4d9', highlightbackground='#12a49d', fg='white', width=10)
label3.place(relx=0.25, rely=0.75)

entry = Entry(upper_frame, font=FONT, fg='#001a4d')
entry.place(relx=0.45, rely=0.75)

# button
button1 = Button(root, text='Convert', font=FONT, bg='pink', fg='black', activeforeground='pink',
                 activebackground='black', command=lambda: convert(clicked1.get(), clicked2.get(), entry.get()))
button1.place(relx=0.13, rely=0.4, relwidth=0.15, relheight=0.07)

button2 = Button(root, text='Clear', font=FONT, bg='pink', fg='black', activeforeground='pink',
                 activebackground='black', command=clear)
button2.place(relx=0.32, rely=0.4, relwidth=0.15, relheight=0.07)

button3 = Button(root, text='Reference', font=FONT, bg='pink', fg='black', activeforeground='pink',
                 activebackground='black', command=Help)
button3.place(relx=0.52, rely=0.4, relwidth=0.15, relheight=0.07)

button4 = Button(root, text='Exit', font=FONT, bg='pink', fg='black', activeforeground='pink',
                 activebackground='black', command=Exit)
button4.place(relx=0.72, rely=0.4, relwidth=0.15, relheight=0.07)


root.mainloop()
