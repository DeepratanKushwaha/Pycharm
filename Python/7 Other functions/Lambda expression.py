"""
def evenodd(a):
    if a % 2 == 0:
        print("Even number", a)
    else:
        print("Odd number", a)


evenodd(100)
evenodd(101)
"""
# ---------------------------------------

result = lambda a: print("this number is even:", a % 2 == 0)

result(100)
result(101)
