"""
* * * * *
  *     *
    *   *
      * *
        *
"""

for row in range(5):
    for col in range(5):
        if row == 0 or (col == 4 and row != 0) or (row == 1 and col == 1) or (row == 2 and col == 2) \
                or (row == 3 and col == 3):
            print('*', end='')
        else:
            print(end=' ')
    print()
