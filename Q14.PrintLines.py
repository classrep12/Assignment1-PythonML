
# Write a program that reads multiple lines of input from the user until they 
# enter an empty line, then prints all the lines.
with open("demo.txt",'w') as f:
    line=input("enter line ")
    while(line):
        f.write(line +'\n')
        line=input("enter line ")
with open("demo.txt",'r') as f:
     for line in f:
        print(line,end='')


