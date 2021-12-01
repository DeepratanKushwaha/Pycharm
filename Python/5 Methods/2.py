
def sum(a, b):
    print("Sum of {}+{}={}".format(a, b, a + b))


def multiplication(a, b):
    print("Multiplication: {}*{}={}".format(a, b, a * b))


# calling the method

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
sum(a, b)

a = int(input("Enter 1st number:"))
b = int(input("Enter 2nd number:"))
multiplication(a, b)
