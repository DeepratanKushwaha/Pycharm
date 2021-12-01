"""
a = int(input("Enter 1st number"))
b = int(input("Enter 2nd number"))

if(a>b):
    print("a is greater:",a)
else:
    print("b is greater:",b)
"""

x = 8
r = x % 2

if r == 0:
    print("Even")
    if x > 9:
        print("Great")
    else:
        print("Not so great")

else:
    print("Odd")

print("Bye")
