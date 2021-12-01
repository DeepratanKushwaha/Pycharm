"""
def square(a):
    return a * a


result = square(5)
print(result)
"""

x = lambda a: a * a
result = x(5)
print(result)

x = lambda a, b: a + b
result = x(5, 6)
print(result)
