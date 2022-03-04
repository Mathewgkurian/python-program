
16.	Sort dictionary in ascending and descending order.


import operator
d = {"n": 2, "k": 4, "u": 3, "y": 1, "z": 0}
print('Original dictionary : ',d)
sorted_d = sorted(d.items(),key=operator.itemgetter(1)) print('Dictionary in ascending order by value : ',sorted_d) sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))
print('Dictionary in descending order by value : ',sorted_d)
