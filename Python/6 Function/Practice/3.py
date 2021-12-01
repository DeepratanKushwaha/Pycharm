# sum of first n natural number using recursion

def nsum(num):
    if num == 0:
        return 0

    return num + nsum(num-1)


num = int(input("Enter the number"))
sum = nsum(num)
print(sum)
