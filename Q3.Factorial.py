# Write a python program that calculates the factorial of a given number.

num = int(input("Enter any number : "))
factorial = 1;
for i in range(1,num+1):
    factorial *= i
print("The factorial of",num ,"is : ", factorial)
