import re

str = "Ball,Mall,Call,Hall,waterfall,fairfall,fairall"

print(str)

# pattern object
result = re.compile("[f]all")
# it will compile a regular expression pattern into expression object
print(result)

s = result.sub("MALL", str)  # substitute method
print(s)
