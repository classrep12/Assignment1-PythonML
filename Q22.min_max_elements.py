#. Write a python program that returns the minimum and maximum values 
# in a list of numbers.
l=eval(input("enter the list"))
c=0
num=int(input("enter the element"))
for i in l:
    if i==num:
        c+=1
print(num," occurs ",c," times ")