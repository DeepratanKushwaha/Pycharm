for row in range(7):
    for col in range(5):
        if (row == 0 or row == 3 or row == 6) and (0 < col < 4) or (col == 0 and (0 < row < 3))\
                or (col == 4 and (3 < row < 6)):
            print('*', end='')
        else:
            print(end=' ')
    print()
