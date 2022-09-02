a = int(input("Enter a : "))
b = int(input("Enter b : "))
print("Before Swapping : " )
print("a = ", a)
print("b = ", b)

#old way : -
# temp = a
# a = b
# b = temp

# python way :-
a,b=b,a
print("After Swapping : " )
print("a = ", a)
print("b = ", b)