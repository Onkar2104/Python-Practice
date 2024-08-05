from array import *

rollno=array('i',[9,10,20,15,10])
print(rollno[0])
print(rollno[1])
print(rollno[2])
print(rollno[3])
print(rollno[4])

print("--for loop--")
n = len(rollno)
for x in range(n):
    print(rollno[x])

print("--while loop--")
x=0
while(x<n):
    print(rollno[x])
    x+=1