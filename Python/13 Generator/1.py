"""
Generator Function :- A generator function defined like a normal function, but whenever it needs to generate a value,
                      It does so with the 'yield' keyword rather than return. If the body of def contains 'yield', the
                      function automatically becomes generator function.
"""


def simpleGeneratorFun():
    yield 1
    yield 2
    yield 3


for value in simpleGeneratorFun():
    print(value)


"""
Generator Object :- Generator function returns a generator object. Generator objects are used either by calling the 
                    next method on the generator object or using the generator object in a 'for in' loop.
"""


def simpleGeneratorFun2():
    yield 1
    yield 2
    yield 3


x = simpleGeneratorFun2()
print(x.__next__())
print(x.__next__())
print(x.__next__())

# A generator function returns an generator object that is iterable, can be used as an iterator.
