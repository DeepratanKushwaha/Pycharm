

a = 10                          # global variable(access anywhere)
print(id(a))


def something():
    a = 15                     # local variable(can't use outside the function)

    x = globals()['a']
    print(id(x))
    print("in fun:", a)

    globals()['a'] = 20         # change the value of global variable


something()

print("outside fun:", a)
print(id(a))
