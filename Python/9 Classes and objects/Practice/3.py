class Sample:
    a = "Deep"


obj = Sample()
obj.a = "Deepratan"     # it will not affect the class attribute it will create instance of a

print(Sample.a)
print(obj.a)

Sample.a = "Deepratan"              # way to change class attribute/variable
print(Sample.a)
