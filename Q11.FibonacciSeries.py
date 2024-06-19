#  Write a python program that generates the first n numbers in the Fibonacci sequence.
num = int(input("Enter any no : "))
n1 = 0
n2 = 1
next_no = n2
count =1
while count <= num:
    print(next_no, end= " ")
    count += 1
    n1 , n2 = n2, next_no
    next_no = n1 + n2 
print()