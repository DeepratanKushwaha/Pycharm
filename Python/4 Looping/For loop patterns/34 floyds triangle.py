num = int(input('Enter the number of rows : '))
n = 1
for row in range(1, num+1):
    for col in range(1, row+1):
        print(n, end=' ')
        n += 1
    print()
