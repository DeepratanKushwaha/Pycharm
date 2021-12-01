# use open function to read content from the file

f = open('sample.txt', 'r')   # by default mode is read
data = f.read(10)
print(data)

f.close()
