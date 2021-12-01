"""
Iterator in python is any type of python type that can be used with 'for in loop'.
Python list, tuple, dictionaries and sets are all example of iterator.
But it is not necessary that an iterator object has to exhaust, sometime it can be infinite.
Such type of iterators are known as Infinite iterators.
"""
# three type of infinite iterators

# 1. count(start, step) :- this iterator start printing from the "start" number and prints infinitely.
#                       if steps are mentioned, the numbers are skipped else step is 1 by default

import itertools

for i in itertools.count(5, 5):
    if i == 35:
        break
    else:
        print(i, end=" ")


# 2. cycle(iterable) :- This iterable prints all the values in order from the passed container.
#                       It restart printing from beginning again when all elements are printed in a cycle manner.
print()

count = 0
for i in itertools.cycle('AB'):
    if count > 7:
        break
    else:
        print(i, end=" ")
        count += 1

print()

l1 = ['Geeks', 'for', 'Geeks']

iterator = itertools.cycle(l1)

for i in range(6):
    print(next(iterator), end=" ")

print()

# 3. repeat(val, num) :- This iterator repeatedly prints the passed value infinite number of times
#                        if the optional keyword is mentioned, then it repeatedly prints num numbers of times

print("printing number repeatedly: ")
print(list(itertools.repeat(25, 4)))

