with open('this.txt') as f:
    content = f.read()


with open('copy of this.txt', 'w') as f:
    f.write(content)