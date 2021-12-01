# find maximum of the number in a list using reduce function

from functools import reduce

l1 = [2, 5, 8, 9, 10]

a = reduce(max, l1)
print(a)