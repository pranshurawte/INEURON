# Write a python program to create a School class and 3 instance variables and 1 class variable.

class School :
    principal = "Pooja"

    def __init__(self) :
        self.p = "PhysicsWallah"
        self.c = "Rahi"
        self.m = "Rathi"

    def show(self) :
        print(self.p,self.c,self.m)

Vindhyachal = School()
Vindhyachal.show()
print(School.principal)




