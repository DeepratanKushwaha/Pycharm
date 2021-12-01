
l1 = ['deep', 1, 4, 6, "hello", 4.5, "python"]

for i, items in enumerate(l1):
    if i == 2 or i == 4 or i == 6:
        # print(i, items)
        print(f"The {i + 1}th element is {items}")

