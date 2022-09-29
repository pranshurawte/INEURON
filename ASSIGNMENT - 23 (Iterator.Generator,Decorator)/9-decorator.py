# Define a function which takes lengths of three sides of a triangle as arguments and display the perimeter of triangle. Define and apply a decorator which checks for the validity of the triangle on the basis of lengths of the side. This makes the perimeter to be displayed when the triangle can exist with the given lengths of the sides.


def decor_perimeter(perimeter_func) :
    def calculations(a,b,c) :
        if a + b > c and b + c > a and a + c > b :
            print("Triangle can be formed") 
            perimeter(a,b,c)
        else :
            print("Triangle can not be formed") 
    return calculations        
        
           
@decor_perimeter
def perimeter(a,b,c) :
    print( "The Perimeter is : " , a + b + c)

print("Enter the length of the side of the Triangle")
a = int(input("Enter a :"))
b = int(input("Enter b :"))
c = int(input("Enter c :")) 
perimeter(a,b,c)
