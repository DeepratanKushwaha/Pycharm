# read text from a given file poem.txt and find out whether it contains the word 'twinkle'

f = open('poem.txt')
data = f.read()
if 'twinkle' in data:
    print("twinkle is present")
else:
    print("twinkle is not present")

f.close()