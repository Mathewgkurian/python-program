Write a Python program to read a file line by line and store it into a list.
CODE :
list =[]
f = open("demofile.txt" , 'r')
for x in f:
 print(x)
 list.append(x)
print("the list is ", list)