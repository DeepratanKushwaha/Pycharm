class A:

    def show(self):
        print("in A show")


class B(A):

    def show(self):
        print("in B show")


a1 = B()                                # firstly it checks inside the sub class for show method then called the method
a1.show()                               # if don't find then it will go to super class
