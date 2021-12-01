from array import *

vals = array('i', [1, -2, 3, 4, 5, -6])

new_arr = array(vals.typecode, (a for a in vals))

for i in new_arr:
    print(i)
