class A:  # super class, Parent class

    def Feature1(self):
        print("Feature 1 working")

    def Feature2(self):
        print("Feature 2 working")


class B(A):  # sub class, child class                # Single level
    def Feature3(self):
        print("Feature 3 working")

    def Feature4(self):
        print("Feature 4 working")


class C(B):                                          # multi level
    def Feature5(self):
        print("Feature 5 working")


a1 = A()
b1 = B()
c1 = C()
a1.Feature1()
a1.Feature2()

b1.Feature1()
b1.Feature2()
b1.Feature3()
b1.Feature4()

c1.Feature1()
c1.Feature2()
c1.Feature3()
c1.Feature4()
c1.Feature5()


class D:  # super class, Parent class

    def Feature6(self):
        print("Feature 6 working")

    def Feature7(self):
        print("Feature 7 working")


class E:  # sub class, child class
    def Feature8(self):
        print("Feature 8 working")

    def Feature9(self):
        print("Feature 9 working")


class F(D, E):                                          # multiple Inheritance
    def Feature10(self):
        print("Feature 10 working")


d1 = D()
e1 = E()
f1 = F()

