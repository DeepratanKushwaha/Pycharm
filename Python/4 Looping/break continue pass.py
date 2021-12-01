"""using break statement we can stop the loop before
  it has looped through all the items
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        break
    print(x)


"""using continue statement we can stop the current iteration of the loop
   and continue with the next
"""
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        continue
    print(x)
