# instance method  Class method  Static method
class Student:
    school = "Telusko"

    def __init__(self, m1, m2, m3):
        self.m1 = m1  # instance variables
        self.m2 = m2
        self.m3 = m3

    def avg(self):  # instance method cause we are
        return (self.m1 + self.m2 + self.m3) / 3  # passing self that belongs to particular object

    """
        def get_m1(self):
            return self.m1      # Accessor Method, type of instance method #fetch the value of instance variable

        def set_m1(self, value):
            self.m1 = value         # Mutator Method, type of instance ....change value of instance variable
    """

    @classmethod
    def getschool(cls):  # class method uses for work with class variable
        return cls.school

    @staticmethod
    def info():
        print("this is static method")


s1 = Student(12, 13, 14)
s2 = Student(34, 54, 23)

print(s1.avg())
print(s2.avg())

print(Student.getschool())
Student.info()
