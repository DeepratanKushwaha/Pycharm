from functools import reduce

"""def is_even(n):
    return n % 2 == 0
                                          # filter() function                  

nums = [3, 4, 5, 6, 7, 2, 5, 9, 2]

even = list(filter(is_even, nums))
print(even)
"""

nums = [3, 4, 5, 6, 7, 2, 5, 9, 2]

even = list(filter(lambda a: a % 2 == 0, nums))
print(even)


"""def update(b):
    return b * 2
                                            # map() function

doubles = list(map(update, even))
print(doubles)
"""

doubles = list(map(lambda b: b * 2, even))
print(doubles)


"""def add_all(c, d):
    return c + d
                                            # reduce() function

sum = reduce(add_all, doubles)
print(sum)
"""


sum = reduce(lambda c, d: c+d, doubles)
print(sum)
