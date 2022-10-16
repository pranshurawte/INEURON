# Write a python script to handle a ValueError
import math

try:
    print(math.sqrt(-1))
except ValueError:
    print("ValueError : You can not get take the square root of a negative number")