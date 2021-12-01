"""
5
4 4
3 3 3
2 2 2 2
1 1 1 1 1
"""

num = int(input())
for row in range(num, 0, -1):
    for col in range(num-row+1):
        print(row, end=' ')
    print()
