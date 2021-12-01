content = True
i = 1
with open('log.txt') as f:
    while content:
        content = f.readline().lower()

        if 'python' in content:
            print(content)
            print("Yes python is present")
            print(i)
        i += 1
