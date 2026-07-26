class Laptop:
    def build(self):
        print("Laptop Builds")
class Alien:
    def code(self,machine:Laptop):
        print("Alien Codes")
        machine.build()

class Desktop:
    def build(self):
        print("Desktop Builds")

asus_rog = Laptop()

alien = Alien()
alien.code(asus_rog)
alien.code(Desktop())