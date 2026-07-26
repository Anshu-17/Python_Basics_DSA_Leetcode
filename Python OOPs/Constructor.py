class car:
    def __new__(cls, *args, **kwargs):
        print("new called")
        return super(car, cls).__new__(cls)

    def __init__(self, brand, model, year):
        self.brand = brand # instance variables
        self.model = model # instance variables
        self.year = year # instance variables

    def display(self):
        print(f"{self.brand} {self.model} {self.year}")

    @classmethod
    def info(cls):
        print("This is a car class")
    
    @staticmethod
    def add(x, y):
        return x + y

car1 = car("Toyota", "Camry", 2022)
car2 = car("Honda", "Accord", 2023)

car1.display()
car2.display()
