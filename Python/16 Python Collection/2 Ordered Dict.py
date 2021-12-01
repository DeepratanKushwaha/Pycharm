"""
OrderedDict :- is a dictionary subclass that remembers the order that the keys were inserted first. the only difference
               btw dict() and OrderedDict that:
               OrderedDict preserve the order in which the keys are inserted. A regular dict doesn't track the insertion
               order, and iterating it gives the values in an arbitrary order. By contrast, the order the item are
               inserted is remembered by OrderDict.
"""

from collections import OrderedDict

print('This is a dict:\n')

d = {}
d['a'] = 1
d['b'] = 2
d['c'] = 3
d['d'] = 4

for key, value in d.items():
    print(key, value)

print("\nThis is OrderedDict:\n")
od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
    print(key, value)

# Important Points --

# 1. Key value change :- if the value of a certain key is changed, the position of the key is unchanged in OrderedDict.

from collections import OrderedDict

print("Before:\n")

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
    print(key, value)

print("\nAfter:\n")

od['c'] = 5

for key, value in od.items():
    print(key, value)

# 2. Deletion and Re-inserting :- deletion and re-inserting the same key will push it to the back as OrderedDict,
#                                 however maintains the order of insertion.

from collections import OrderedDict

print("Before deleting:\n")

od = OrderedDict()
od['a'] = 1
od['b'] = 2
od['c'] = 3
od['d'] = 4

for key, value in od.items():
    print(key, value)

print("\nAfter deletion:\n")

od.pop('c')
for key, value in od.items():
    print(key, value)

print("\nAfter re-inserting")

od['c'] = 3

for key, value in od.items():
    print(key, value)
