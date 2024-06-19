#Write a python program that removes all punctuation from a given string
import string
str1=input("enter the string")
str2=""
for c in str1:
    if c not in string.punctuation :
        str2+=c

str1=str2
print(str2)