sample_list = ['chalk', 'duster', 'board', 'pen']
# desired output : chalk and duster and board and pen

# avoid this
for i in sample_list:
    if i != "pen":
        print(i, "and ", end="")
    else:
        print(i)

# use join function
print(" and ".join(sample_list))
