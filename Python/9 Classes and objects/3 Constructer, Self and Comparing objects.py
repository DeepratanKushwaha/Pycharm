class Computer:
    def __init__(self):
        self.name = "Deep"
        self.age = 21

    def update(self):
        self.age = 30

    def compare(self, other):
        if self.age == other.age:
            return True
        else:
            return False


c1 = Computer()
c2 = Computer()

# c1.name = "Raj"
c1.age = 20

if c1.compare(c2):
    print("they are same")
else:
    print("they are different")

# c1.update()         # passing self inside () # importance of self

print(c1.name, c1.age)
print(c2.name, c2.age)
