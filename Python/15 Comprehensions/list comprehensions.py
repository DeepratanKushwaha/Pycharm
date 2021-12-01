# list comprehension is an elegant way to create lists based on existing lists

a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
"""
b = []
for i in a:
    if i % 2 == 0:
        b.append(i)

print(b)
"""

b = [i for i in a if i % 2 == 0]
print(b)
