"""
Counter is a container included in the collections module. Containers are objects that hold object. They provide a way
to access the contained objects and iterate over them. Example of builtin containers are tuple, list, and dictionary.
Others are included in Collection module.
A counter is a subclass of dict. Therefore it is an unordered collection where elements and their respective count are
stored as a dictionary.

syntax: class collection.counter([iterable-or-mapping])

Initialization:
* with sequence of items
* with dictionary containing keys and counts
* with keyword argument mapping string names to count
"""
import collections
from collections import Counter
# with sequence of item
print(Counter(['b', 'b', 'a', 'b', 'c', 'a', 'b', 'b', 'a', 'c']))

# with dictionary
print(Counter({'a': 3, 'b': 5, 'c': 2}))

# with keyword argument
print(Counter(a=3, b=5, c=2))


# Updation: we can also create an empty counter in the following manner.
# count = collections.Counter()
# and can be updated via update() method
# count.update(data)

from collections import Counter
count = Counter()

count.update([1, 1, 3, 1, 5, 2, 2, 8, 3, 5])
print(count)

count.update([1, 2, 9])
print(count)

# data can be provided in any of the three ways as mentioned in initialization and the counter's data will be
# increased not replaced. Counts can be zero and negative also.

from collections import Counter

c1 = Counter(A=4, B=3, C=10)
c2 = Counter(A=10, B=3, C=4)

c1.subtract(c2)
print(c1)

# we can use counter to count distinct elements of a list or other collections.

from collections import Counter

z = ['blue', 'red', 'blue', 'yellow', 'blue', 'red']
print(Counter(z))
