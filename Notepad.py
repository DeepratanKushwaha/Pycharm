from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os


def newFile(event=None):
    global file
    root.title("Untitled - Notepad")
    file = None
    textarea.delete(1.0, END)


def openFile(event=None):
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()


def saveFile(event=None):
    global file
    if file is None:
        file = asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"),
                                                                                                 ("Text Documents",
                                                                                                  "*.txt")])
        if file == "":
            file = None
        else:
            # save as new file
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file) + " - Notepad")
            print("File Saved")
    else:
        # save the file
        f = open(file, "w")
        f.write(textarea.get(1.0, END))
        f.close()


def quitApp():
    root.destroy()


def cut(event=None):
    textarea.event_generate("<<Cut>>")


def copy(event=None):
    textarea.event_generate("<<Copy>>")


def paste(event=None):
    textarea.event_generate("<<Paste>>")


def about():
    showinfo("Notepad", "Notepad by Deep")


if __name__ == '__main__':
    root = Tk()
    root.title("My Notepad")
    root.geometry("700x500")
    #root.wm_iconbitmap('notepad.ico')
    # Add text area
    textarea = Text(root, font="ariel 11", undo=True)
    file = None
    textarea.pack(expand=True, fill=BOTH)

    # create menu bar
    menuBar = Menu(root)

    # file menu start
    fileMenu = Menu(menuBar, tearoff=0)

    fileMenu.add_command(label="New", command=newFile, accelerator="Ctrl+N")
    fileMenu.add_command(label="Open...", command=openFile, accelerator="Ctrl+O")
    fileMenu.add_command(label="Save", command=saveFile, accelerator="Ctrl+S")
    fileMenu.add_command(label="Save as...", command=None)

    fileMenu.add_separator()

    fileMenu.add_command(label="Page Setup...", command=None)
    fileMenu.add_command(label="Print...", command=None)

    fileMenu.add_separator()

    fileMenu.add_command(label="Exit", command=quitApp)

    menuBar.add_cascade(label="File", menu=fileMenu)
    # file menu end

    # edit menu start
    editMenu = Menu(menuBar, tearoff=0)

    editMenu.add_command(label="Undo", command=textarea.edit_undo, accelerator='Ctrl+Z')

    editMenu.add_separator()

    editMenu.add_command(label="Cut", command=cut, accelerator='Ctrl+X')
    editMenu.add_command(label="Copy", command=copy, accelerator='Ctrl+C')
    editMenu.add_command(label="Paste", command=paste, accelerator='Ctrl+V')
    editMenu.add_command(label="Delete", command=None)

    editMenu.add_separator()

    editMenu.add_command(label="Find...", command=None)
    editMenu.add_command(label="Find Next", command=None)
    editMenu.add_command(label="Replace...", command=None)
    editMenu.add_command(label="Go TO...", command=None)

    editMenu.add_separator()

    editMenu.add_command(label="Select All", command=None)
    editMenu.add_command(label="Time/Date", command=None)

    menuBar.add_cascade(label="Edit", menu=editMenu)
    # edit menu ends

    # format menu start
    formatMenu = Menu(menuBar, tearoff=0)

    formatMenu.add_command(label="Word Wrap", command=None)
    formatMenu.add_command(label="Font...", command=None)

    menuBar.add_cascade(label="Format", menu=formatMenu)
    # format menu ends

    # view menu start
    viewMenu = Menu(menuBar, tearoff=0)

    viewMenu.add_command(label="Status Bar", command=None)
    menuBar.add_cascade(label="View", menu=viewMenu)

    # help menu starts
    helpMenu = Menu(menuBar, tearoff=0)

    helpMenu.add_command(label="View Help", command=about)
    helpMenu.add_separator()
    helpMenu.add_command(label="About Notepad", command=about)
    menuBar.add_cascade(label="Help", menu=helpMenu)
    # help menu ends

    root.config(menu=menuBar)

    # Adding ScrollBar
    scroll = Scrollbar(textarea)
    scroll.pack(side=RIGHT, fill=Y)
    scroll.config(command=textarea.yview)
    textarea.config(yscrollcommand=scroll.set)

    root.bind('<Control-n>', newFile)
    root.bind('<Control-o>', openFile)
    root.bind('<Control-s>', saveFile)
    root.bind('<Control-x>', cut)
    root.bind('<Control-c>', copy)
    root.bind('<Control-v>', paste)
    root.bind('<Control-z>', textarea.edit_undo)

    root.mainloop()
