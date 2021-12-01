"""
Generator expression :- In python, to create iterators , we can use both regular functions and generators.
                        Generators are written like a normal function but we use 'yield' instead of 'return' for
                        searching a result. It is more powerful as a tool to implement iterators. It is easy and more
                        convenient to implement because it offers the evaluation of elements on demand. Unlike regular
                        function which on encountering a return statement terminates entirely, generator used the yield
                        statement in which the state of the function is saved from the last call and can be picked up
                        or resumed the next time we call a generator function. Advantage of generator over a list is
                        that it takes much less memory. In addition to that, two more functions __next__() and
                        __iter__() make the generator function more compact and reliable.
"""


def generator():
    t = 1
    print('first result is', t)
    yield t

    t += 1
    print('Second result is', t)
    yield t

    t += 1
    print('Third result is', t)
    yield t


call = generator()
next(call)
next(call)
next(call)


"""
    There are various other expressions that can be simply coded similar to list comprehensions but instead of bracket 
    we use parenthesis. These expression are designed for situation where the generator is used right away by an 
    enclosing function. Generator expression allows creating a generator without a yield keyword.
"""

# generator expression

generator = (num**2 for num in range(10))
for num in generator:
    print(num)


# we can also generate a list using generator expressions.

string = 'geek'
li = list(string[i] for i in range(len(string)-1, -1, -1))
print(li)
