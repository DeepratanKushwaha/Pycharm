class Student:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def add(self, a=None, b=None, c=None):

        d = 0

        if a is not None and b is not None and c is not None:   # method overloading is not supported in python
            d = a + b + c                                       # so we are doing by this way
        elif a is not None and b is not None:
            d = a + b
        else:
            d = a

        return d


s1 = Student(4, 5)

print(s1.add(5, 1, 3))
