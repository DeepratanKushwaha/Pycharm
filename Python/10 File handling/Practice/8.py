file1 = "this.txt"
file2 = "copy of this.txt"      # try log.txt

with open(file1) as f:
    f1 = f.read()


with open(file2) as f:
    f2 = f.read()


if f1 == f2:
    print("Files are identical")
else:
    print("Files are not identical")
