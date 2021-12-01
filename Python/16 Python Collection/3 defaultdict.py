"""
defaultdict is an unordered collection of data values that are used to store data values like map. Unlike other data
types that holds only single value as an element, the dictionary holds key:value pair in dictionary, the key must be
unique amd immutable. this means a python tuple can be a key whereas a python list can not. A dictionary can be created
by placing a sequence of element with curly braces {} separated by comma.
"""

Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'}
print("Dictionary:")
print(Dict)
print(Dict[1])
# print(Dict[4])          # Key Error

"""
Some time the key error is raised, it might become a problem. To overcome this we use defaultdict which is present 
inside the collection module.
"""

# Defaultdict :-  syntax :- defaultdict(default_factory)
# default_factory :- a function returning a default value for the dictionary defined. if this argument is absent then
#                    the KeyError is raised.

from collections import defaultdict


def def_value():
    return "Not Present"


d = defaultdict(def_value)
d['a'] = 1
d['b'] = 2

print(d['a'])
print(d['b'])
print(d['c'])


"""
inner working of defaultdict :-
                                defaultdict adds one writable instance variable and one method in addition to the 
                                standard dictionary operation. the instance variable is the 'default_factory' parameter
                                and the method provided is __missing__.
"""

from collections import defaultdict

d = defaultdict(lambda: "Not Present")
d['a'] = 1
d['b'] = 2

print(d['a'])
print(d['b'])
print(d['c'])

""" 
__missing__() :- this function is used to provide the default value for the dictionary. this function takes default 
                 default_factory as an argument and if this argument is None, a key error is raised otherwise it 
                 provides a default value for the giving key. this method is basically called by the __getitem__()
                 method of the dict class when the requested key is not found. __getitem__() raised or return the value 
                 returned by the __missing__() method.
"""

from collections import defaultdict

d = defaultdict(lambda: "Not Present")
d['a'] = 1
d['b'] = 2

# providing default value for the key

print(d.__missing__('a'))
print(d.__missing__('d'))


# using list as default_factory :- when the list class is passed as default factory argument, then a defaultdict is
#                                  created with the values that are list.

from collections import defaultdict

d = defaultdict(list)
for i in range(5):
    d[i].append(i)

print("Dictionary with values as list:")
print(d)


# using int as default_factory :- when the int class is passed as default_factory, then a defaultdict is created with
#                                 default value zero.

from collections import defaultdict

d = defaultdict(int)
L = [1, 2, 3, 4, 2, 4, 1, 2]

for i in L:                 # iterate through the list for keeping the count
    d[i] += 1               # the default value is zero so no need to enter the first key

print(d)
