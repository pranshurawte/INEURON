# Write a python program to init default values for user object using __init__ method.

class user :
    def __init__(self ) :
        self.a = 5
        self.b = 6

    def show(self) :
        print(self.a , self.b)    

obj1 = user()

user.show(obj1)