# find greatest of three number using function

def maximum(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            return num1
        else:
            return num3
    else:
        if num2 > num3:
            return num2
        else:
            return num3


x = maximum(56567, 4556, 3445)
print("max value is", x)
