# demo of STRING handling in python
s1 = "we are learning python at RAT"
print(type(s1))
print(s1)
print("s1[4] is::", s1[4])
print(s1[7:])  # slice operator
print(s1[7:15])
print(s1 + s1)
print(s1 * 3)
print(s1[-1])
print(s1[-2])
print(s1[-3])
print(s1[::-1])
print(s1[::-2])
print(s1[::2])
print(s1.capitalize())
print(s1.startswith("we"))
print(s1.endswith("RAT"))
print(s1.count('a'))
print(s1.count('t'))
print(s1.isalpha())  # isalpha function return true for alphabet without space otherwise false

s2 = "       Machine Learning     "
print(s2)
print(s2.strip())