

def fib(n):
    a = 0
    b = 1

    if n < 0:
        print("Negative values are not allowed")
    elif n == 0:
        print("Please enter value greater than 0 ")
    elif n == 1:
        print(a)
    else:
        print(a)
        print(b)

        for i in range(2, n):
            c = a + b
            a = b                   # swap values
            b = c                   # swap values

            print(c)


x = int(input("Enter the number for fibonacci sequence:"))
fib(x)
