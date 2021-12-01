import tkinter as tk
import pyautogui

win = tk.Tk()
win.title("Take Screenshot")
win.geometry("300x300")


def takeScreenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save('screenshot.png')


button = tk.Button(win, text="Capture Screenshot", command=takeScreenshot)
button.pack()

win.mainloop()
