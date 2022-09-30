# Write a python program to create 2 objects of the user class and assign different values.

class user :
    def __init__(self, a , b) :
        self.a = a
        self.b = b

    def show(self) :
        print(self.a , self.b)    

obj1 = user(1,2)
obj2 = user(3,4)
user.show(obj1)
user.show(obj2)


