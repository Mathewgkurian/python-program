19.	From a list of integers, create a list removing even numbers.

list1=[]
print("enter number") for i in range(0,5):
x=int(input()) list1.append(x)
print(list1) for i in list1:
if i%2==0:
list1.remove(i) print(list1)
