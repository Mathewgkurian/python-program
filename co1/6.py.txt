
6.	Enter 2 lists of integers. Check (a) Whether list are of same length (b) whether list sums to same value (c) whether any value occur in both

list1=[1,23,34,345,6,77,5]
list2=[4,56,778,3,4,55,23,78,88,9]
print("length of list1:",len(list1)) print("length of list1:",len(list2)) if len(list1)==len(list2):
print("both list have same length") else:
print("both list are of different length")
z=0 c=0
for i in list1: z=z+i
print("sum of the values of list 1 is:",z) for i in list2:
c=c+i
print("sum of the values of list 2 is:",c) if(z!=c):
print("list sum is not same") else:

print("list sum is same") for g in range(0,len(list1)):
if list1[g] in list2: print(list1[g],"occur in both")
