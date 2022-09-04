# Write a python program to Swap two tuples in Python.

t1 = ("Java" , "Python" , "SQL" , "C")
t2 = ("Flutter " , "Dart" , "Android" , "Hive")
temp = ()

print("Before Swapping")
print(" t1 = " , t1)
print(" t2 = " , t2)

temp = t1
t1 = t2
t2 = temp

print("After Swapping")
print(" t1 = " , t1)
print(" t2 = " , t2)

