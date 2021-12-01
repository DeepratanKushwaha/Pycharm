from tkinter import *

root = Tk()
root.geometry("500x400")
root.title("Scroll Bar")

# for connecting scrollbar to a widget
# 1. widget(yscrollcommand = scrollbar.set)
# 2. scrollbar.config(command=widget.yview)


scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(root, yscrollcommand=scrollbar.set)
for i in range(300):
    listbox.insert(END, f"Item {i}")
listbox.pack(fill=BOTH, padx=20, pady=20)
scrollbar.config(command=listbox.yview)

root.mainloop()
