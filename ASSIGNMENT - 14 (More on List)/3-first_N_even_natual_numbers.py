# Write a Python script to create a list of first N even natural numbers.

n = int(input("Enter a number  : "))
l2 = [ ele for ele in range(2 , (n * 2 )+ 1 , 2)]
print(l2)