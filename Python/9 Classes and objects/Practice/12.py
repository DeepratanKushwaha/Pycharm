# write class vector representing a vector of n dimension
# overload the + and * which calculate sum and dot product of them
# override __len__() method to display the dimension of vector


class Vector:
    def __init__(self, vec):
        self.vec = vec

    def __str__(self):
        str1 = ''
        index = 0
        for i in self.vec:
            str1 += f"{i} a{index} +"
            index += 1
        return str1[:-1]

    def __add__(self, other):
        newList = []
        for i in range(len(self.vec)):
            newList.append(self.vec[i] + other.vec[i])
        return Vector(newList)

    def __mul__(self, other):
        sum = 0
        for i in range(len(self.vec)):
            sum += self.vec[i] + other.vec[i]
        return sum

    def __len__(self):
        return len(self.vec)


v1 = Vector([1, 2, 3, 4, 5])
v2 = Vector([6, 7, 8, 9, 10])

print(v1 + v2)
print(v1 * v2)

print(len(v1))
print(len(v2))
