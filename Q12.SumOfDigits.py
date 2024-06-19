#  Write a python program that calculates the sum of the digits of a given number.
num = int(input("Enter any number :"))
def sumOfDigits(num):
    sum = 0
    for i in str(num):
        sum = sum + int(i)
    return sum
print(sumOfDigits(num))