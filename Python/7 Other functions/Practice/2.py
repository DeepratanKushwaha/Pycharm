# filter a list of numbers which are divisible by 5

l1 = [1, 2, 5, 10, 45, 4, 6, 8, 35, 75, 95]

filter1 = list(filter(lambda a:a % 5 == 0, l1))
print(filter1)