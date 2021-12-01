def greet():
    print("hello")
    print("good morning")


def add(x, y):
    c = x + y
    return c


greet()
result = add(5, 6)
print(result)


def add_sub(x, y):
    c = x + y
    d = x - y
    return c, d


result1, result2 = add_sub(5, 4)
print(result1, result2)
