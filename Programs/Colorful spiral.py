import turtle

colors = ['red', 'yellow', 'green', 'purple', 'blue', 'orange']     # defining color

t = turtle.Pen()        # setup turtle pen

t.speed(10)             # change the speen of turtle

turtle.bgcolor("black")  # bg color

# make spiral web
for x in range(250):
    t.pencolor(colors[x % 6])   # setting color
    t.width(x/100 + 1)          # setting width
    t.forward(x)                # moving forward
    t.left(55)                  # moving left

turtle.done()
