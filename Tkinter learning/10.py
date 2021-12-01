from tkinter import *

root = Tk()
root.title("Fcuk Yuo")
canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")
can_widget = Canvas(root, width=canvas_width, height=canvas_height)
can_widget.pack()

# the line goes from the point x1, y1 to x2, y2
can_widget.create_line(0, 0, 800, 400, fill="blue")
can_widget.create_line(0, 400, 800, 0, fill="green")

# to create rectangle specify parameters in this order- cooords of top left and coords of bottom right
can_widget.create_rectangle(70, 30, 20, 20, fill="blue")

can_widget.create_text(45, 24, text="python")

can_widget.create_oval(300, 200, 200, 300)

root.mainloop()
