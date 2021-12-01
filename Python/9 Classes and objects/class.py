class Demo:
    a = 100  # class variable

    def show(self):
        print("show method called")


d = Demo()
print(d)
d.show()
print("a is :", Demo.a)

print("------------")
d1 = Demo()
print(d1)
