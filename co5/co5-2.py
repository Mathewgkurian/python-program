Python program to copy odd lines of one file to other
CODE :
fn = open('demofile.txt', 'r')
fn1 = open('demo2.txt', 'w')
cont = fn.readlines()
type(cont)
for i in range(0, len(cont)):
 if (i % 2 != 0):
 fn1.write(cont[i-1])
 else:
 pass
fn1.close()
fn1 = open('demo2.txt', 'r')
cont1 = fn1.read()
print(cont1)
fn.close()
fn1.close()