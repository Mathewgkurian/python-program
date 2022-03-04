3.	Write a Python program to read each row from a given csv file and print a list of strings



import csv
with open('people.csv', 'r') as file: reader = csv.reader(file)
for row in reader: print(row)


people.csv

SN, Name, City
1, Michael, New Jersey 2, Jack, California
