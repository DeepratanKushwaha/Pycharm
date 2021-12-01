# user defined objects(using OOPS)

class Counter:
    def __init__(self, start, end):
        self.num = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.num > self.end:
            raise StopIteration
        else:
            self.num += 1
            return self.num


# driver code

if __name__ == '__main__':
    a, b = 2, 5
    c1 = Counter(a, b)
    c2 = Counter(a, b)

# way 1 to print range without iter()

print("Print the range without iter()")
for i in c1:
    print("Eating more pizzas, counting", i, end="\n")

# way 2 using iter()

print("\n Print the range using iter()\n")

obj = iter(c2)
try:
    while True:
        print("Eating more pizzas, counting", next(obj))
except:
    # when StopIteration raised , print custom message
    print("\n Dead on overFood, GAME OVER")
