class A: # parent class
    def f1(self):
        print("f1 called")
    def f2(self):
        print("f2 called")
    def show(self):
        print("show from A called")

class B: # child class of A
    def f3(self):
        print("f3 called")
    def show(self):
        print("show from B called")

class C(B): # child class of B
    def f4(self):
        print("f4 called")

class D(B,A): # child class of A and B
    def f5(self):
        print("f5 called")
    #def show(self):
        #print("show from D called")

obj1 = A()
obj2 = B()
obj3 = C()
obj4 = D()

obj4.show() # MRO(Method Resolution Order) -> B,A,Object -> D,B,A,Object

print(D.mro())
