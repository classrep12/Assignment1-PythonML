# Write a program that reads the content of a text file and prints it to the console.
f=open("string.txt","w")
s=input("enter a string ")
f.write(s)
f.close()
f=open("string.txt","r")
data=f.read()
print("The read data is :")
print(data)
f.close()