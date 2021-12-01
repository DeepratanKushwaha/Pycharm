# finditer function is similar

import re

str = "road ahead technologies, road ahead infotech road ahead"
result = re.finditer("road", str)

for i in result:
    print(i)
    index = i.span()
    print("index is", index)
