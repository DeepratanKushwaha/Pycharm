# multiplication table of given number using for loop

num = int(input("Enter the number"))
for i in range(1, 11):
    print(str(num) + "x" + str(i) + "=" + str(num * i))
    # or
    # print(f"{num}X{i}={num*i}")


# multiplication table of given number using while loop

num = int(input("Enter the number"))
i = 1
while i <= 10:
    print(num*i)
    i += 1


# multiplication table of given number using for loop in reversed order

num = int(input("Enter the number"))
for i in range(10, 0, -1):
    print(str(num) + "x" + str(i) + "=" + str(num * i))
    # or
    # print(f"{num}X{i}={num*i}")
