# Write a Python script to store a list of city names in a file ‘cities.txt’
f = open("cities.txt","w")
names = "Bhopal Gwalior Indore Sehore"

print(names)
f.write(names)
f.close()