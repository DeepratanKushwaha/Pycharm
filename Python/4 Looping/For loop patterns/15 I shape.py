for row in range(7):
    for col in range(5):
        if (row == 0 or row == 6) or col == 2 and (0 < row < 6):
            print('*', end='')
        else:
            print(end=' ')
    print()
