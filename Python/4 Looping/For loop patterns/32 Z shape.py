for row in range(4):
    for col in range(4):
        if row == 0 or row == 3 or (row == 1 and col == 2 or row == 2 and col == 1):
            print('*', end='')
        else:
            print(end=' ')
    print()

