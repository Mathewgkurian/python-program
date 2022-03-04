5 Store a list of first names. Count the occurrences of ‘a’ within the list

list1=[] z=0
limit=int(input("enter limit")) print("enter first names")
for i in range(0,limit): data=str(input()) list1.append(data)
print(list1)
for i in range(0,limit): x=list1[i].count('a') z=z+x
print("number of 'a' in the list is: ",z)
