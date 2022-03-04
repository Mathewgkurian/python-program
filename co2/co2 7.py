7.	Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly’

string = input("enter word:") if len(string) < 3:
print(string)
elif string[-3:] == 'ing': print(string + 'ly')
else:
print(string + 'ing')

