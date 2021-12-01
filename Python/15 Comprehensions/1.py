"""
List Comprehension
Dictionary Comprehension
Set Comprehension
13 Generator 15 Comprehensions
"""


list1 = [1, 32, 4, 45, 4, 4, 3, 3, 3, 5, 6, 3, 5, 6, 343, 5, 9]
divideby3 = []
for i in list1:
    if i % 3 == 0:
        divideby3.append(i)
print('without using list comprehensions', divideby3)

print('using list comprehensions', [i for i in list1 if i % 3 == 0])

# dict
dict1 = {'a': 45, 'b': 65, 'A': 5}
print({k.lower(): dict1.get(k.lower(), 0) + dict1.get(k.upper(), 0) for k in dict1.keys()})

# set
squared = {x ** 2 for x in [1, 2, 3, 4, 4, 4, 5, 5, 5, 5, 6]}
print(squared)

# generator
gen = (i for i in range(55) if i % 2 == 0)
for item in gen:
    print(item, end=" ")
