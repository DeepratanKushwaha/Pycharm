
i = 1
while i <= 30:
    print("i is:", i)
    i += 1

print("outside the loop!!")


i = 1  # initialization

while i <= 5:  # condition
    print("Deep", i)
    i += 1  # increment

i = 5  # initialization

while i >= 1:  # condition
    print("Deep", i)
    i -= 1  # increment

# take 10 int value from user using loop and print their average value

sum = 0
i = 1
while i <= 10:
    x = int(input("Enter number:"))
    sum = sum + x
    i += 1
print("average is:", sum/10)