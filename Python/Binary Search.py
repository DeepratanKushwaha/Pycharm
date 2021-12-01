pos = -1


def Search(list, n):
    l = 0
    u = len(list) - 1

    while l <= u:
        mid = (l + u) // 2

        if list[mid] == n:

            globals()['pos'] = mid
            return True
        else:
            if list[mid] < n:
                l = mid + 1
            else:
                u = mid - 1
    return False


list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 345, 657, 76554, 4353]
n = int(input())

if Search(list, n):
    print("Found at", pos+1)
else:
    print("Not Found")
