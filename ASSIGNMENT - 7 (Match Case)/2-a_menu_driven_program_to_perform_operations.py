a = int(input("Enter a : "))
b = int(input("Enter b : "))
print("Operations Menu : \n","1.Addition","2.Subtraction","3.Multiplication","4.Division" ,"Enter your choice : ",sep = "\n")
num = int(input())

match num :
    case 1 : 
        print("The sum is ", a + b )
    case 2 : 
        print("The difference is ", a - b )
    case 3 : 
        print("The product is ", a * b )
    case 4 : 
        print("The answer is ", a / b )
    case _ :
        print("Invalid Operation")    