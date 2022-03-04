Create a class Time with private attributes hour, minute and second. Overload ‘+’
operator to find sum of 2 time
CODE :
class Time:
 __hour = 0
 __minute = 0
 __second = 0
 def input_time(self, hour, m, s):
 self.hour = hour
 self.minute = m
 self.second = s
 def __add__(self, obj):
 day = 0
 sec1 = self.second + obj.second
 mins = sec1 // 60
 sec1 = sec1 % 60
 min1 = self.minute + obj.minute + mins
 hrs = min1 // 60
 min1 = min1 % 60
 hour1 = self.hour + obj.hour + hrs
 day = hour1 // 24
 hour1 = hour1 % 24
 return "{}:{}:{}:{}".format(day, hour1, min1, sec1)
t1 = Time()
t2 = Time()
print("enter first time")
hh = int(input("enter hour"))
mm = int(input("enter minute"))
ss = int(input("enter second"))
t1.input_time(hh, mm, ss)
print("enter second time")
hh = int(input("enter hour"))
mm = int(input("enter minute"))
ss = int(input("enter second"))
t2.input_time(hh, mm, ss)
print(t1 + t2)