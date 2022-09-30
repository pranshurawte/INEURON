# Write a python program to create 3 User objects and find the youngest of all.

class User :
    def __init__(self, age ) :
        self.age = age
        

    def show(self) :
        print(self.age )  

    def compare(self,s2,s3) :
        if self.age > s2.age and self.age > s3.age :
            print(self.age)
        elif s2.age > self.age and s2.age > s3.age :
            print(s2.age)
        else :
            print(s3.age)
    

obj1 = User(12)
obj2 = User(3)
obj3 = User(7)
User.compare(obj1,obj2,obj3)
obj1.compare(obj2,obj3)
