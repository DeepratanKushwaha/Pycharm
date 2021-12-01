

def fact(n):

    if n == 0:
        return 1

    return n * fact(n-1)


x = int(input("Enter number to find factorial:"))
Factorial = fact(x)
print("Factorial is: {}".format(Factorial))
