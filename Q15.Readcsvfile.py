# . Write a program that reads data from a CSV file and prints it to the console.
import csv
with open("new_file1.csv",'r',newline='\n') as f:
    reader_object=csv.reader(f,delimiter='/')
    for line in reader_object:
        print(line)