# Write a Python script to create a list of first N odd natural numbers.

n = int(input("Enter a Number  : "))
l1 = [ ele for ele in range(1 , n * 2 , 2)]
print(l1)