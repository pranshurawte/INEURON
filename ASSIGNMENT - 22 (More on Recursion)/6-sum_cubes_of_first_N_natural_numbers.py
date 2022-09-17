# Write a recursive python function to calculate sum of cubes of first N natural numbers

def cube_sum( num ) :
    if num == 1 :
        return 1
    return num**3 + cube_sum(num - 1)


print(cube_sum(int(input("Enter a Number : "))))    
