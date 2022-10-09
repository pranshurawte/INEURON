# Write a python script to update 2nd Question, add a class variable (platform) and create a classmethod to access it.


class Profile :
    platform = "Ineuron"

    def __init__(self,name,email,age) :
        self.name = name
        self.email = email
        self.age = age
    
    @classmethod
    def show2(cls):
        print(cls.platform)

    def show(self):
        print(self.name,self.email,self.age,sep = "\n")
        
        

P1 = Profile("Pranshu","kravate35@gmail.com",20)
# P1.show()
Profile.show2()