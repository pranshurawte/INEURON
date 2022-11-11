# Write a Python script to create a new file ‘myfile.txt’ and store user entered text.

f = open("file1.txt","w")   #here f referes to file objecgt
text = input("Enter your text : ")
f.write(text)
f.close()