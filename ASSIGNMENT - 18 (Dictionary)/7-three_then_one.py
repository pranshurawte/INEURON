# Write a python program to create three dictionaries, then create one dictionary that will contain the other three dictionaries.

d1 = {"name" : "Pranshu" , "age" : 19 , "gender"  : "Male "}
d2 = {"name" : "Ankit" , "age" : 20 , "gender"  : "Male "} 
d3  ={"name" : "Nitesh" , "age" : 18 , "gender"  : "Male "}

d4 = {}
d4[0] = d1
d4[1] = d2
d4[2] = d3
print(d4)