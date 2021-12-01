for row in range(5):
    for col in range(5):
        if row == 0 and (col == 0 or col == 4) or row == 1 and (col == 1 or col == 3) or (col == 2 and row > 1):
            print('*', end='')
        else:
            print(end=' ')
    print()
