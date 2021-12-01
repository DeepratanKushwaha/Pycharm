# python function to print multiplication table of given number

def table(num):
    for i in range(1, 11):
        print(num*i)


num = int(input("Enter the number"))
table(num)
