2.	Create a package graphics with modules rectangle, circle and sub-package 3D-graphics with modules cuboid and sphere. Include methods to find area and perimeter of respective figures in each module. Write programs that finds area and perimeter of figures by different importing statements. (Include selective import of modules and import * statements)

area and perimeter.py
from graphics import rectangle from graphics import circle
from graphics.threedpackage.cuboid import *

#*********rectangle******** num1=int(input("enter length of rectangle:")) num2=int(input("enter breadth of rectangle:")) res1=rectangle.area(num1,num2)
print("area of rectangle:",res1) res2=rectangle.perimeter(num1,num2)

print("perimeter of rectangle:",res2)


#*********circle********

rad=int(input("enter radius of circle:")) res3=circle.area(rad)
print("area of circle:",res3) res4=circle.perimeter(rad)

print("perimeter of circle:",res4)

#*********cuboid********

l=int(input("enter length of cuboid:")) b=int(input("enter breadth of cuboid:")) h=int(input("enter hieght of cuboid:"))

res3=area(l,b,h)
print("area of cuboid:",res3) res2=perimeter(l,b) print("perimeter of cuboid:",res2)

#*********sphere********
from graphics.threedpackage.sphere import * r=int(input("enter radius of sphere"))


res4=area(r)
print("area of sphere:",res4)
 

res5=perimeter(r)
print("perimeter of sphere:",res5)





circle.py

def area(rad): res3=3.14*rad*rad return res3
def perimeter(rad): res4=2*3.14*rad return res4
rectangle.py

def area(num1,num2): res1=num1*num2 return res1
def perimeter(num1,num2): res2=2*(num1+num2) return res2
cuboid.py

def area(l,b,h): res5=2*(l*b+b*h+h*l) return res5
def perimeter(l,b): res2=2*(l+b) return res2
sphere.py

def area(l,b,h): res5=2*(l*b+b*h+h*l) return res5
def perimeter(l,b): res2=2*(l+b) return res2
