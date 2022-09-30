# WRT 7th Question, create 3 Laptop objects and add them to the list in the sorted
# order based on the ram size.

class Laptop :
    def __init__(self,brand,ram,cpu,hdd) :
        self.brand = brand
        self.ram = ram
        self.cpu = cpu
        self.hdd = hdd

    def showConfig(self):
        print(self.brand , self.ram , self.cpu , self.hdd) 

    def arrange(self,s2,s3) :
        mylist =[self.ram,s2.ram,s3.ram]
        mylist = sorted(mylist)
        print(mylist)


mylaptop1 = Laptop("ASUS",4,"i7","1TB")  
mylaptop2 = Laptop("Hp",16,"i7","0TB")  
mylaptop3 = Laptop("ASUS",8,"i7","1TB")  
mylaptop1.arrange(mylaptop2,mylaptop3)