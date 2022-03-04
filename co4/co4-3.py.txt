Create a class Rectangle with private attributes length and width. Overload ‘<’ operator
to compare the area of 2 rectangles.
CODE :
class Rectangle():
 def __init__(self, l, w):
 self.length= l
 self.width = w
 def rectangle_area(self):
 return self.length * self.width
 def __lt__(self, other):
 if(self.rectangle_area()<other.rectangle_area()):
 return True
 else:
 return False
l1 = int(input("enter length of the rectangle 1 : "))
w1 = int(input("enter width of the rectangle 1: "))
l2 = int(input("enter length of the rectangle 2 : "))
w2 = int(input("enter width of the rectangle 2: "))
Rectangle1= Rectangle(l1, w1)
Rectangle2= Rectangle(l2,w2)
print("area of first rectangle :",Rectangle1.rectangle_area())
print("area of second rectangle :",Rectangle2.rectangle_area())
if Rectangle1 < Rectangle2:
 print("Rectangle two is large")
else:
 print("Rectangle one is large or these are equal")