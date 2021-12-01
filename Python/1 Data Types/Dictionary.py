""""It contains key value pair encloesd with { }
    Value can be of any data type but the key should be of STRING or INTEGER type
    and must be unique
"""

students = {1: "Deep", 2: "Harsh", "three": "Rohit", 4: "Dinesh", 5: "Era"}
print(students)
print(type(students))
students[2] = "Priyanka"
print(students)
students[3] = "Candy"
students["three"] = "Diksha"
print(students)

print(students.keys())    # to get all keys
print(students.values())  # to get all values
print(students.items())   # to get all items from list
print(students.get(1))    # to get item having key you give
