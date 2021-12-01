# using while loop
pos = -1


def Search(list, n):
    i = 0
    while i < len(list):
        if list[i] == n:
            globals()['pos'] = i
            return True
        i += 1
    return False


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 5

if Search(list, n):
    print("Found at", pos+1)
else:
    print("Not Found")


# using for loop
pos = -1


def Search(list, n):
    i = 0
    for i in list:
        if list[i] == n:
            globals()['pos'] = i
            return True
    return False


list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
n = 5

if Search(list, n):
    print("Found at", pos+1)
else:
    print("Not Found")


