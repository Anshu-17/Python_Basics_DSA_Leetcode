class A: # parent class
    def __init__(self):
        print("A init called")
    def f1(self):
        print("f1 called")
    def f2(self):
        print("f2 called")
    def show(self):
        print("show from A called")

class B(A):
    def __init__(self):
        super().__init__()
        print("B init called")
    def f3(self):
        super().f1()
        print("f3 called")
    def f4(self):
        print("f4 called")
    def show(self):
        print("show from B called")

# Every class in python is a child class of object class
obj1 = A()
print(A.__base__)
print("--------------------------------------")
obj2 = B()
obj2.f1() #it will call init of A class if B class doesn't have init method

# if B class has init method then it will call init of B class
# if B class doesn't have init method then it will call init of A class
# if B class doesn't have init method and A class doesn't have init method then it will call init of object class

#SuperClass
print("--------------------------")
obj2 = B()
obj2.f1()