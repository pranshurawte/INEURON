print("Menu : ")
print("a. Check whether a given set of three numbers are lengths of an isosceles triangle or not")
print("b. Check whether a given set of three numbers are lengths of sides of a right angled triangle or not")
print("c. Check whether a given set of three numbers are equilateral triangle or not")
print("d. Exit.")
alpha = input()
print()

first_side  = int(input("Enter the length of first side : "))
second_side = int(input("Enter the length of second side : "))
third_side = int(input("Enter the length of third side : "))


match alpha :
    case 'a' :
        if first_side == second_side or third_side == second_side or first_side == third_side :
            print("Isosceles Triangle ")
        else :
            print("Not an Isosceles Triangle")    
    case 'c' : 
        if first_side == second_side == third_side :
            print("Equilaternal Triangle")
        else :
            print("Not an equilateral Triangle")   
    case 'b' :
        if first_side ** 2 == second_side ** 2 + third_side ** 2 or second_side ** 2 == first_side ** 2 + third_side ** 2 or third_side ** 2 == first_side ** 2 + second_side ** 2 :
            print("Right Angled Triangle")    
        else : 
            print("Not a right angled Triangle")  
    case 'd' :
        print("Exit")              


