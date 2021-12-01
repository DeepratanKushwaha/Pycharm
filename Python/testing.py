z
exit()

import numpy

arr = tuple(map(int, input().split()))
print(numpy.zeros(arr))
print(numpy.ones(arr))

exit()

import numpy

N, M = map(int, input().split())

arr = numpy.array([input().split() for i in range(N)], int)
print(arr.transpose())
print(arr.flatten())


import numpy as np
arr = input().split()
a = np.array(arr, int)
a1 = np.reshape(a, (3, 3))
print(a1)


n = int(input())
arr = list(map(int, input().split()))
z = max(arr)
if max(arr) == z:
    arr.remove(max(arr))
print(max(arr))


n = int(input())
arr = map(int, input().split())
print(sorted(set(arr))[-2])

# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import product

l1 = input().split(" ")
l2 = input().split(" ")

pr = product(l1, l2)
print(int(pr))

exit()

import operator
import time

l1 = [1, 2, 3]
l2 = [2, 3, 4]

t1 = time.time()

a, b, c = map(operator.mul, l1, l2)

t2 = time.time()

print("Result: ", a, b, c)
print("time taken by map function ", t2 - t1)

t1 = time.time()
print("Result:", end="")
for i in range(3):
    print(l1[i] * l2[i], end="")

t2 = time.time()

print("\ntime taken by for loop ", t2 - t1)
