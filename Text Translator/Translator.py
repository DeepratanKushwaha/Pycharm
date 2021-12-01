from tkinter import *
from tkinter.ttk import Combobox
from tkinter import messagebox
from textblob import TextBlob

root = Tk()
root.geometry("500x400")
root.title("Translator")
root.resizable(0, 0)
root.configure(bg="turquoise1")
root.iconbitmap("translator.ico")
lan_dict = {'afrikaans': 'af', 'albanian': 'sq', 'amharic': 'am', 'arabic': 'ar', 'armenian': 'hy', 'azerbaijani': 'az',
            'basque': 'eu', 'belarusian': 'be', 'bengali': 'bn', 'bosnian': 'bs', 'bulgarian': 'bg', 'catalan': 'ca',
            'cebuano': 'ceb', 'chichewa': 'ny', 'chinese (simplified)': 'zh-cn', 'chinese (traditional)': 'zh-tw',
            'corsican': 'co', 'croatian': 'hr', 'czech': 'cs', 'danish': 'da', 'dutch': 'nl', 'english': 'en',
            'esperanto': 'eo', 'estonian': 'et', 'filipino': 'tl', 'finnish': 'fi', 'french': 'fr', 'frisian': 'fy',
            'galician': 'gl', 'georgian': 'ka', 'german': 'de', 'greek': 'el', 'gujarati': 'gu',
            'haitian creole': 'ht', 'hausa': 'ha', 'hawaiian': 'haw', 'hebrew': 'he', 'hindi': 'hi', 'hmong': 'hmn',
            'hungarian': 'hu', 'icelandic': 'is', 'igbo': 'ig', 'indonesian': 'id', 'irish': 'ga', 'italian': 'it',
            'japanese': 'ja', 'javanese': 'jw', 'kannada': 'kn', 'kazakh': 'kk', 'khmer': 'km', 'korean': 'ko',
            'kurdish (kurmanji)': 'ku', 'kyrgyz': 'ky', 'lao': 'lo', 'latin': 'la', 'latvian': 'lv',
            'lithuanian': 'lt', 'luxembourgish': 'lb', 'macedonian': 'mk', 'malagasy': 'mg', 'malay': 'ms',
            'malayalam': 'ml', 'maltese': 'mt', 'maori': 'mi', 'marathi': 'mr', 'mongolian': 'mn',
            'myanmar (burmese)': 'my', 'nepali': 'ne', 'norwegian': 'no', 'odia': 'or', 'pashto': 'ps',
            'persian': 'fa', 'polish': 'pl', 'portuguese': 'pt', 'punjabi': 'pa', 'romanian': 'ro', 'russian': 'ru',
            'samoan': 'sm', 'scots gaelic': 'gd', 'serbian': 'sr', 'sesotho': 'st', 'shona': 'sn', 'sindhi': 'sd',
            'sinhala': 'si', 'slovak': 'sk', 'slovenian': 'sl', 'somali': 'so', 'spanish': 'es', 'sundanese': 'su',
            'swahili': 'sw', 'swedish': 'sv', 'tajik': 'tg', 'tamil': 'ta', 'telugu': 'te', 'thai': 'th',
            'turkish': 'tr', 'ukrainian': 'uk', 'urdu': 'ur', 'uyghur': 'ug', 'uzbek': 'uz', 'vietnamese': 'vi',
            'welsh': 'cy', 'xhosa': 'xh', 'yiddish': 'yi', 'yoruba': 'yo', 'zulu': 'zu'}


def Click(event=None):
    try:
        word = TextBlob(varName1.get())
        lan = word.detect_language()
        lanToDict = languages.get()
        lanTo = lan_dict[lanToDict]
        word = word.translate(from_lang=lan, to=lanTo)
        label3.configure(text=word)
        varName2.set(word)
    except:
        label3.configure(text="Check your internet connection or Try another keyword")


def Exit():
    rr = messagebox.askyesnocancel('Notification', 'Are you sure you want to exit ?', parent=root)
    if rr:
        root.destroy()


# binding function

def entryEnter1(event):
    entry1['bg'] = 'springgreen'


def entryLeave1(event):
    entry1['bg'] = 'white'


def entryEnter2(event):
    entry2['bg'] = 'springgreen'


def entryLeave2(event):
    entry2['bg'] = 'white'


def btnEnter1(event):
    btn1['bg'] = 'springgreen'


def btnLeave1(event):
    btn1['bg'] = 'yellow'


def btnEnter2(event):
    btn2['bg'] = 'springgreen'


def btnLeave2(event):
    btn2['bg'] = 'yellow'


# Combo Box

languages = StringVar()
lan_box = Combobox(root, width=30, textvariable=languages, state='readonly')
lan_box['values'] = [e for e in lan_dict.keys()]
lan_box.current(37)
lan_box.place(x=300, y=0)

# Entry Box
varName1 = StringVar()
entry1 = Entry(root, textvariable=varName1, font="times 15 italic bold", width=30)
entry1.place(x=150, y=40)

varName2 = StringVar()
entry2 = Entry(root, textvariable=varName2, font="times, 15 italic bold", width=27)
entry2.place(x=150, y=100)

# Label

label1 = Label(root, text="Enter Word : ", font="times 15 italic bold", relief=GROOVE)
label1.place(x=5, y=40)

label2 = Label(root, text="Translated : ", font="times 15 italic bold", relief=GROOVE)
label2.place(x=5, y=100)

label3 = Label(root, text='', font="times 15 italic bold", bg="turquoise1")
label3.place(x=10, y=250)

# button
clickImg = PhotoImage(file="clicking.png")
exitImg = PhotoImage(file="exit.png")

clickImg = clickImg.subsample(15, 15)
exitImg = exitImg.subsample(18, 18)

btn1 = Button(root, text="Click", bg='yellow', activebackground='red', bd=10, width=100, font="times 15 italic bold",
              image=clickImg, compound=RIGHT, command=Click)
btn1.place(x=70, y=170)
root.bind('<Return>', Click)

btn2 = Button(root, text="Exit", bg='yellow', activebackground='red', bd=10, width=100, font="times 15 italic bold",
              image=exitImg, compound=RIGHT, command=Exit)
btn2.place(x=280, y=170)

# Binding

entry1.bind('<Enter>', entryEnter1)
entry1.bind('<Leave>', entryLeave1)

entry2.bind('<Enter>', entryEnter2)
entry2.bind('<Leave>', entryLeave2)

btn1.bind('<Enter>', btnEnter1)
btn1.bind('<Leave>', btnLeave1)

btn2.bind('<Enter>', btnEnter2)
btn2.bind('<Leave>', btnLeave2)

root.mainloop()
