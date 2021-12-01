# positional/required argument
def person(name, age):
    print(name)
    print(age)


person("deep", 20)


# keyword argument
def person1(name, age):
    print(name)
    print(age-5)


person1(age=20, name="deep")


# default argument
def person2(name, age=20):        # age=20 default argument
    print(name)
    print(age)


person2("deep", 21)                 # 21 will overwrite


# variable length argument
def add(a, *b):

    c = a
    for i in b:
        c = c + i
    print("add is:", c)


add(5, 6, 7, 8, 9)


# or

def add(*b):
    c = 0
    for i in b:
        c = c + i
    print("add is:", c)


add(5, 6, 7, 8, 9)
