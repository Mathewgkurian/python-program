2.	List comprehensions: (a) Generate positive list of numbers from a given list of integers
(b) Square of N numbers (c) Form a list of vowels selected from a given word (d) List ordinal value of each element of a word (Hint: use ord() to get ordinal values)


#LIST OF POSITIVE NUMBERS#
positive=[2,-1,4,56,-67,0,45,-356,44]
list1=[]
for i in positive: if i>0:
list1.append(i) print(list1)
#	# #LIST OF SQUARE NUMBERS# numbers=[3,4,5,6,7,8,9,2,1]
list2=[]
for x in numbers: x=x**2 list2.append(x)
print(list2)
#	# #LIST OF VOWEL#
x="thiruvanadhapuram" list3=[]
for i in x:
if i=='a' or i=='A' or i=='e' or i=='E' or i=='o' or i=='O' or i=='u' or i=='U' or i=='i' or i=='I':
list3.append(i) print(list3)
#	# #LIST OF ORDINAL VALUES#
s="martin" list4=[] for i in s:
list4.append(ord(i)) print(list4)

