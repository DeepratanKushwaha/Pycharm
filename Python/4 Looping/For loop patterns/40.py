"""
1
2 1
3 2 1
4 3 2 1
5 4 3 2 1
"""

num = int(input())
for row in range(1, num+1):
    for col in range(row, 0, -1):
        print(col, end=' ')
    print()
