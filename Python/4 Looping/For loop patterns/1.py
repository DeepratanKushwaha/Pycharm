
num = int(input("Enter the number of rows"))
for i in range(1, num+1):  # rows
    for j in range(1, i+1):  # cols
        print("*", end=" ")
    print()  # for new line


num = int(input("Enter the number of rows"))
for i in range(num, 0, -1):
    for j in range(0, i):
        print("*", end=" ")
    print()

