
for row in range(7):
    for col in range(6):
        if ((col == 0 or col == 5) and row != 0) or ((row == 0 or row == 3) and (0 < col < 5)):
            print('*', end='')
        else:
            print(end=' ')
    print()