# write class complex to represent complex number along with overloaded operator + and * which adds and multiplies them
# formula = (ac- bd) + (ad + bc)i
#           real part   imaginary part

class Complex:
    def __init__(self, r, i):
        self.real = r
        self.imaginary = i

    def __add__(self, other):
        return Complex(self.real + other.real, self.imaginary + other.imaginary)

    def __mul__(self, other):
        mulReal = self.real * other.real - self.imaginary * other.imaginary
        mulImg = self.real * other.imaginary + self.imaginary  * other.real
        return Complex(mulReal, mulImg)

    def __str__(self):
        if self.imaginary < 0:
            return f"{self.real} - {-self.imaginary}i"
        else:
            return f"{self.real} + {self.imaginary}i"


c1 = Complex(1, -2)
c2 = Complex(19, -7)

print(c1 + c2)
print(c1 * c2)
