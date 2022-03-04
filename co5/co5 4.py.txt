4.	Write a Python program to read specific columns of a given CSV file and print the content of the columns.

#

import csv

colum_name=input("Enter Column name:") with open('username.csv','r') as csvf:
data=csv.DictReader(csvf,delimiter=",") print("conten of "+colum_name+" is ") for row in data:
print(row[colum_name])



username.csv

department_id,department_name,manager_id,location_id 10,Administration,200,1700
20,Marketing,201,1800 30,Purchasing,114,1700 40,Human Resources,203,2400 50,Shipping,121,1500 60,IT,103,1400
70,Public Relations,204,2700 80,Sales,145,2500
90,Executive,100,1700
