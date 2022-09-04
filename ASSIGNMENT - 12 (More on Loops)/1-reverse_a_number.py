# Write a python script to reverse a number.
num = (input("Enter a Number : "))
num2  = int(num)
reverse = 0 
for var in num :
    reverse *= 10
    reverse = reverse +  num2 % 10
    num2 = num2 //10 
print(reverse)    
