from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.geometry("800x600+250+50")
root.minsize(width=800, height=600)
root.maxsize(width=800, height=600)
root.configure(bg="powder blue")
root.title("Typing Speed Game")
# root.iconbitmap("abc.ico")

words = ['Mango', 'Apple', 'gun', 'fan', 'door', 'tv', 'laptop', 'mobile']


def labelSlider():
    global count, sliderWords
    text = "Welcome to typing speed game"
    if count >= len(text):
        count = 0
        sliderWords = ''
    sliderWords += text[count]
    count += 1
    fontLabel.configure(text=sliderWords)
    fontLabel.after(150, labelSlider)


def startGame(event):
    global score, miss
    if timeLeft == 14:
        time()
    gamePlayDetailLabel.configure(text='')
    if wordEntry.get() == wordLabel['text']:
        score += 1
        scoreLabelCount.configure(text=score)
    else:
        miss += 1
    random.shuffle(words)
    wordLabel.configure(text=words[0])
    wordEntry.delete(0, END)


def time():
    global timeLeft, score, miss
    if timeLeft <= 5:
        timerLabelCount.configure(fg='red')
    if timeLeft > 0:
        timeLeft -= 1
        timerLabelCount.configure(text=timeLeft)
        timerLabelCount.after(1000, time)
    else:
        gamePlayDetailLabel.configure(text=f"Hit = {score} | Miss = {miss} | Total Score = {score-miss}")
        rr = messagebox.askretrycancel('Notification', 'Hit Retry to play again')
        if rr:       # or if rr == True:
            score = 0
            timeLeft = 14
            miss = 0
            timerLabelCount.configure(text=timeLeft)
            wordLabel.configure(text=words[0])
            scoreLabelCount.configure(text=score)


score = 0
miss = 0
timeLeft = 14
count = 0
sliderWords = ''

random.shuffle(words)
fontLabel = Label(root, text="", font="arial 25 italic bold", bg="powder blue", fg="red", width=40)
fontLabel.place(x=10, y=10)
labelSlider()


wordLabel = Label(root, text=words[2], font="arial 25 italic bold", bg="powder blue")
wordLabel.place(x=350, y=200)

scoreLabel = Label(root, text="Your Score :", font="arial 25 italic bold", bg="powder blue")
scoreLabel.place(x=10, y=100)

scoreLabelCount = Label(root, text="0", font="arial 25 italic bold", bg="powder blue", fg="blue")
scoreLabelCount.place(x=80, y=180)

timerLabel = Label(root, text="Time Left :", font="arial 25 italic bold", bg="powder blue")
timerLabel.place(x=600, y=100)

timerLabelCount = Label(root, text=timeLeft, font="arial 25 italic bold", bg="powder blue", fg="blue")
timerLabelCount.place(x=680, y=180)

gamePlayDetailLabel = Label(root, text="Type word and hit enter", font="arial 30 italic bold",
                            bg="powder blue", fg="dark grey")
gamePlayDetailLabel.place(x=150, y=450)

wordEntry = Entry(root, font="arial 40 italic bold", bg="powder blue", bd=10, justify='center')
wordEntry.place(x=100, y=300)
wordEntry.focus_set()

root.bind('<Return>', startGame)
root.mainloop()
