# constructor behave, super(), method resolution order(MRO)
class A:
    def __init__(self):
        print("in a init")

    def Feature1(self):
        print("Feature 1 A working")

    def Feature2(self):
        print("Feature 2 working")


class B:
    def __init__(self):
        print("in b init")

    def Feature1(self):
        print("Feature 1 B working")

    def Feature4(self):
        print("Feature 4 working")


class C(A, B):
    def __init__(self):
        super().__init__()
        print("in c init")

    def feat(self):
        super().Feature2()


a1 = C()
a1.Feature1()
a1.feat()