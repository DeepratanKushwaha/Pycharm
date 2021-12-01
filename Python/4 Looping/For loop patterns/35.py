"""
p
p y
p y t
p y t h
p y t h o
p y t h o n
"""

string = input()
for row in range(0, len(string)):
    for col in range(0, row+1):
        print(string[col], end=' ')
    print()
