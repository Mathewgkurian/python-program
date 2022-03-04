1.	Display future leap years from current year to a final year entered by user.

import datetime s=datetime.datetime.now() y=s.year
a=0

year=int(input("enter future year")) for i in range(y,year):
if i % 400 == 0 and i % 100 != 0: a=1
print(i)

elif i % 4 == 0: a=1
print(i)
if a==0:
print("can't find any leap year")
