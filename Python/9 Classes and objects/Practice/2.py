# write a class calculator capable of finding square, squareRoot, cube of a number

class Calculator:
    def __init__(self, num):
        self.num = num

    def square(self):
        print(f"The square of {self.num} is {self.num ** 2}")

    def squareRoot(self):
        print(f"The squareRoot of {self.num} is {self.num * 0.5}")

    def cube(self):
        print(f"The cube of {self.num} is {self.num ** 3}")


a = Calculator(4)
a.square()
a.squareRoot()
a.cube()
