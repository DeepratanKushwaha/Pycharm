# the enumerate function adds counter to an iterable and returns it
list = ["deep", 1, 4, "hello", 3.5]

for i, item in enumerate(list):
    print(i+1, item)


a = ['CodeWithHarry', 'T-Series', 'Dude Perfect', 'The Slow Mo Guy']

# avoid this
i = 0
for item in a:
    i += 1
    if i % 2 == 0:
        print(item)

# use enumerate

for i, item in enumerate(a):
    if (i+1) % 2 == 0:
        print(i, item)
