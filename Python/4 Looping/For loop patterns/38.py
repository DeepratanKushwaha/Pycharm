"""
1
1 1
1 1 1
1 1 1 1
1 1 1 1 1
"""
num = int(input())
for row in range(1, num+1):
    for col in range(1, row+1):
        print('1', end=' ')
    print()