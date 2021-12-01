
def top():
    yield 1
    yield 2
    yield 3
    yield 4


values = top()
print(values.__next__())
print(values.__next__())

for i in values:
    print(i)


def tensqrt():
    n = 1

    while n <= 10:
        sq = n * n
        yield sq
        n += 1


value = tensqrt()

for j in value:
    print(j)
