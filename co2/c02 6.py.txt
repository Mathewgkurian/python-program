
6.	Count the number of characters (character frequency) in a string.


s=str(input("enter string:")) dict={}
for i in s:
if i in dict:
dict[i]=dict[i]+1 else:
dict[i]=1 print(dict)

