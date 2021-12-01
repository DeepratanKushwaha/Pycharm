

def person(name, **data):

    print(name)

    for i, j in data.items():
        print(i, j)


person("deep", age=20, city="jaipur", mob=9887410890)