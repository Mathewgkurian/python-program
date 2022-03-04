1.	Work with built-in packages calculator.py
from calculatorfun import add,sub,mul,div num1=int(input("enter first number:")) num2=int(input("enter second number:")) print("\n********menu*********") print("\n1 for addition")
print("\n2 for substration") print("\n3 for multiplication") print("\n4 for divition") cho=int(input("enter your choice:")) if(cho==1):
result=add(num1,num2) print("ans:",result)
elif(cho==2):
result=sub(num1,num2) print("ans:",result)
elif(cho==3):
result=mul(num1,num2) print("ans:",result)
elif(cho==4):
result=div(num1,num2) print("ans:",result)


calculatorfun.py

def add(num1,num2): result=num1+num2 return result
def sub(num1,num2): result=num1-num2 return result
def mul(num1,num2): result=num1*num2 return result
def div(num1,num2): result=num1/num2 return result
