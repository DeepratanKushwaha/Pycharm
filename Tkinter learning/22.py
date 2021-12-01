from tkinter import *
root = Tk()
root.geometry("655x444")
root.title("Title of GUI")
root.wm_iconbitmap("icon.png")
root.configure(background="black")

width = root.winfo_screenwidth()
height = root.winfo_screenheight()

print(f"{width}x{height}")
Button(text="Close", command=root.destroy).pack()

root.mainloop()
