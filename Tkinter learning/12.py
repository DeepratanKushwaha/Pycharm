from tkinter import *
from PIL import Image, ImageTk


def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text += text[i]
        if i % 100 == 0 and i != 0:
            final_text += "\n"
    return final_text


root = Tk()
root.title("News")
root.geometry("1000x1000")

texts = []
photos = []

for i in range(0, 3):
    with open(f"{i+1}.txt") as f:
        text = f.read()
        texts.append(every_100(text))

    image = Image.open(f"{i+1}.png")
    # TODO: resize these images
    image = image.resize((225, 265), Image.ANTIALIAS)
    photos.append(ImageTk.PhotoImage(image))


f1 = Frame(root, width=800, height=70).pack()
Label(f1, text="News", font="lucida 33 bold").pack()
Label(f1, text="April 29 2050", font="lucida 13 bold").pack()

f2 = Frame(root, width=900, height=200).pack(anchor="w")
Label(f2, text=texts[0], padx=22, pady=22).pack(side="left")
Label(f2, image=photos[0], anchor="se").pack()

f3 = Frame(root, width=900, height=200).pack(anchor="w")
Label(f3, text=texts[1], padx=22, pady=22).pack(side="left")
Label(f3, image=photos[1], anchor="e").pack()

f4 = Frame(root, width=900, height=200).pack(anchor="w")
Label(f4, text=texts[2], padx=22, pady=22).pack(side="left")
Label(f4, image=photos[2], anchor="e").pack()


root.mainloop()
