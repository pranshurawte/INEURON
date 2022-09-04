# Write a python program to copy elements 4 and 5 from the following tuple into a new tuple. tuple1=(1,2,3,4,5,6)

tuple1=(1,2,3,4,5,6)

ls = []
ls.append(tuple1[4])
ls.append(tuple1[5])
ls =tuple(ls)
print(ls)
print(type(ls))