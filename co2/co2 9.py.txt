9.	Construct following pattern using nested loop

*
* *
* * *
* * * *
* * * * *
* * * *
* * *
* *
*



n=int(input("enter the limit of the pattern:")) for i in range(n):
for j in range(i):
print ('* ', end="") print('')

for i in range(n,0,-1): for j in range(i):
print('* ', end="") print('')

