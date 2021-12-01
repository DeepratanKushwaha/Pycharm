"""findall function will search
it will search the entire string form left to right
search function scan the string looking for the first location where the regular expression pattrtn produces a batch
    and returns a corresponding batch
if no match found it returns none
match function will search at the beginning of string if no match found it will return none else it will return
the match object
"""

import re

name = "Abhishek roll no is 111, Rajesh roll no is 21, Pooja roll no is 444"

roll = re.findall('/d{1,2}', name)
name = re.findall('[A-Z][a-z]*', name)
# it will match the name starting from capital letter
print(roll)
print(name)

values = {}

x = 0

for str in name:
    values[str] = roll[x]
    x += 1

print(values)

print("\tRAT")
print(r"\tRAT")  # r means row string
