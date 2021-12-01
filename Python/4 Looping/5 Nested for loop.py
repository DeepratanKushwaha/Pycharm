# table printing

import time  # predefined library

for i in range(2, 11):
    for j in range(1, 11):
        print(i * j, end="\t")
    time.sleep(1)  # delay in second
    print()  # for new line

# star pattern

for i in range(5):  # rows
    for j in range(i + 1):  # cols
        print("*", end="\t")

    print()  # for new line

count = 5
for i in range(count):
    for j in range(count, i, -1):
        print("*", end="\t")

    print()
