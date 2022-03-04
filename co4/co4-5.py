Create a class Publisher (name). Derive class Book from Publisher with attributes title
and author. Derive class Python from Book with attributes price and no_of_pages. Write
a program that displays information about a Python book. Use base class constructor
invocation and method overriding.
CODE :
class Publisher:
 def __init__(self,name):
 self.name=name
 def display(self):
 print('Name:',self.name)
class Book(Publisher):
 def __init__(self,title,author):
 self.title=title
 self.author=author
class Python(Book):
 def __init__(self,name,title,author,price,noofpage):
 self.price=price
 self.noofpage=noofpage
 Publisher.__init__(self,name)
 Book.__init__(self, title, author)
 def display(self):
 print('Book Title:',self.title,'\n Author:',self.author,'\nPrice :',self.price,'\n No Of
Pages:',self.noofpage)
n=input("Enter book name")
t=input("title")
a=input("author")
p=int(input("price"))
np=int(input("pages"))
p = Python(n,t,a,p,np)
p.display()