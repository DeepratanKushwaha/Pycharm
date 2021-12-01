"""class Computer:

    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is ", self.cpu, self.ram)


com1 = Computer('i5', 16)
com2 = Computer('i3', 8)

com1.config()
com2.config()
"""


class Demo:
    def __init__(self, a, b):
        print("Cons. Called")
        self.x = a
        self.y = b
        print("a is: ", a)
        print("b is: ", b)

    def add(self):
        print("Sum is", self.x + self.y)

    def multi(self):
        print("Multiplication is", self.x * self.y)


d = Demo(12,12)
d.add()
d.multi()
