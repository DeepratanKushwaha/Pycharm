for row in range(8):
    for col in range(5):
        if ((col == 0 or col == 4) and (row != 0 and row != 6 and row != 7)) or \
                ((row == 0 or row == 6) and (0 < col < 4)) or (col == 1 and row == 5) or (col == 3 and row == 7):
            print('*', end='')
        else:
            print(end=' ')
    print()
