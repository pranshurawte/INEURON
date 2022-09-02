print("Enter value of a , b and c of a quadratic equation")
a,b,c = int(input()) , int(input()) , int(input())
d = b**2 - 4 * a * c
if d > 0 :
    print("Real & Distinct Roots")
elif d == 0 :
    print("Real & Equal Roots")  
else :
    print("Imaginary Roots")      
    