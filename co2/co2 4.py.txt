
4.	Generate a list of four digit numbers in a given range with all their digits even and the number is a perfect square.


 list=[]
num=int(input("enter limit")) for i in range(1000,num+1):
for j in range(32,100): if i==j*j:
s=str(i)
if int(s[0])%2==0 and int(s[1])%2==0 and int(s[2])%2==0 and int(s[3])%2==0:
list.append(i)
print(list)

