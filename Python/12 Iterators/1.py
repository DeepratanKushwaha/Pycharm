"""
At many instances, we need to access an object like an iterator. one way is to form a generator loop but that extends
the task and time taken by programmer. Python eases this task by providing a built-in-method __iter__() for this task.
"""

"""
The __iter__() function returns an iterator for the given object(array, tuple, set etc or custom objects). It creates 
an object that can be accessed one element at a time using __next__() function, which generally comes in handy when 
dealing with loops.
"""

# 1
listA = ['a', 'e', 'i', 'o', 'u']
iter_listA = iter(listA)
try:
    print(next(iter_listA))
    print(next(iter_listA))
    print(next(iter_listA))
    print(next(iter_listA))
    print(next(iter_listA))
    print(next(iter_listA))  # stop iteration error
except:
    pass


# 2
listB = ['Cat', 'Bat', 'Sat', 'Mat']
iter_listB = listB.__iter__()
try:
    print(iter_listB.__next__())
    print(iter_listB.__next__())
    print(iter_listB.__next__())
    print(iter_listB.__next__())
    print(iter_listB.__next__())  # StopIterationError
except:
    print("\n Throwing 'StopIterationError'", "I cannot count more.")


# 3
lst = [11, 22, 33, 44, 55]
iter_lst = iter(lst)

while True:
    try:
        print(iter_lst.__next__())
    except:
        pass
