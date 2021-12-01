num = int(input("Enter the number"))

table = [num * i for i in range(1, 11)]   # list comprehension
print(table)

with open('Table.txt', 'w') as f:
    f.write(str(table))
