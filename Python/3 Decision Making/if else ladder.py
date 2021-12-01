"""
marks = int(input("Enter marks:(0-100)"))
print("Marks:", marks)

if 80 <= marks <= 100:
    print("Grade A")
elif 60 <= marks < 80:
    print("Grade B")
elif 40 <= marks < 60:
    print("Grade C")
elif marks < 40:
    print("Fail")
else:
    print("Wrong Input")
"""

units = int(input("Enter no. of units"))
print("Units:", units)

if 0 < units <= 500:
    print("4rs/piece")
elif 500 < units <= 2000:
    print("4.25rs/piece")
elif 2000 < units <= 5000:
    print("5rs/piece")
elif units > 5000:
    print("7rs/piece")
else:
    print("wrong input")
