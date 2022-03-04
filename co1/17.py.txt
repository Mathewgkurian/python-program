17.	Merge two dictionarie

dict1={} dict2={}
n=int(input("enter limit:")) for i in range(0,n):
keys=input("enter keys:") values=int(input("enter values:")) dict1[keys]=values
print(dict1)
for i in range(0,n): keys1=input("enter keys:")
values1=int(input("enter values:")) dict2[keys1]=values1
print(dict2) dict1.update(dict2) print(dict1)
