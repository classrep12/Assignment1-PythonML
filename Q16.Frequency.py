# 16. Write a program in python that counts the frequency of each character in a string.
str1 = input("Enter any string value : ")
result = {}
for keys in str1:
    result[keys] = result.get(keys,0) + 1

print("The count of all characters in str1 is : \n" + str(result))
