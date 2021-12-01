
def update(x):

    print(id(x))
    print("hello")
    x = 8
    print(id(x))
    print("x", x)


a = 10
print(id(a))
update(a)
print("a", a)


def update(list):
    print(id(list))

    list[1] = 25
    print(id(list))
    print("x", list)


list = [10, 20, 30]
print(id(list))
update(list)
print("list", list)
