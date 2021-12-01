# printing table from 2 to 20. write it to different files

for i in range(2, 21):
    with open(f"multiplication table of {i}.txt", 'w') as f:
        for j in range(1, 11):
            f.write(f"{i}x{j} = {i*j}\n")
