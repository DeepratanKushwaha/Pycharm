class MyError(Exception):
    pass


a = int(input("enter integer number:"))
print("a is :", a)
if a == 3:
    try:
        raise ArithmeticError("wrong input 3, retry")
    except ArithmeticError as e:
        print(e)
else:
    b = 100/(a-3)
    print("b is :", b)


print("end of program")
