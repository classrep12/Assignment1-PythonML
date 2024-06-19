#Write a program that takes a string input from the user and writes it to a text file.
f=open("stringfile.txt","w")
str1=input("enter a string ")
f.write(str1)
f.close()
