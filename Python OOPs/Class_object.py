class computer:
    def __init__(self, cpu, ram, ssd): # __init__ is a special method which is called automatically when an object is created
        print("init called")
        self.cpu = cpu
        self.ram = ram
        self.ssd = ssd

    def config(self): 
        print(f"{self.cpu}, {self.ram}, {self.ssd}")

com1 = computer("i5", "8GB", "512GB") # com1 is Object computer() is constructor(round brackets)
com2 = computer("i7", "16GB", "1TB") # Object

computer.config(com1)
computer.config(com2)

# or

com1.config()
com2.config()

