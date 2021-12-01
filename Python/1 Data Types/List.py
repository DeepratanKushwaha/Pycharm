""""python directly doesn't support array,instead of array we will use list
    List is a collection of items is closed with square bracket
    List are mutable(changeable)
"""
marks = [99, 78, 87, 35, 65, 76, 32, 24, 100]
print(marks)
print("Marks:", marks)
print(marks[3])
print(marks[1:4])
print(marks[3:])
print(marks[::])
print(marks[::-1])
print(marks[::-2])
marks[1] = 20  # list are mutable
print(marks)
print(marks+marks)
print(marks*3)
