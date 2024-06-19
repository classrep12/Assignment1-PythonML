#  Write a python program that takes a list of numbers and returns their sum.
list1 = eval(input("enter the list of numbers"))
s=0
for num in list1:
    s+=num
print("sum of elements in the list : ",s," using sum() method : ",sum(list1))
