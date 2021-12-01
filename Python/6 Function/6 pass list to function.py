"""
def count(lst):
    even = 0
    odd = 0
    for i in lst:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


# taking multiple inputs at a time separated by comma
lst = [int(lst) for lst in input("Enter multiple value: ").split(",")]
print("Number of list is: ", lst)

even, odd = count(lst)
print("Even number are: {} and Odd number are: {}".format(even, odd))
"""


def count1(lst1):
    user = 0

    for i in lst1:
        if len(i) > 5:
            user += 1

    return user


# taking multiple inputs at a time separated by comma
lst1 = [lst1 for lst1 in input("Enter multiple value: ").split(",")]
print("List of name is: ", lst1)

user = count1(lst1)
print("Name having length more then 5 are {}:".format(user))
