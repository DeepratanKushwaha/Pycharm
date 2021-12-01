num = list(range(5, 10))
print(num)

print(list(range(11, 20)))

for i in range(10):
    print("i is:", i)

for i in range(10, 30, 2):
    print("i is:", i)

for i in range(30, 10, -2):
    print("i is:", i)

marks = [33, 44, 55, 66, 77, 88, 99]
sum = 0
for i in marks:
    sum = sum + i
    print(i)

print("total marks:", sum)
print("avg marks:", sum / 7)

print("----------------------")

for i in [22, 33, 44, 55, 66, 77]:
    print("i is:", i)

for i in range(1, 21):
    if i % 5 != 0:
        print(i)
