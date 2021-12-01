# wap a function to remove a given word form a string and strip it at same time

def remove_split(string, word):
    newstring = str.replace(word, "")
    return newstring.strip()


str = "      My self deep ratan     "

new = remove_split(str, "ratan")
print(new)
