#loops

'''loops are the iteration(repeat) statement.
there are 2 types of loops in python.
1.While
2.for

There are 3 steps in loops:
1.Initialize [from where to start]
2. Condition [upto where follow the loop:]
3. Increment/decrement'''


#While-Loop

'''a=1
while(a<= 5):
    print(a)
    a=a+1


#for-loop

for i in range(1,6):
    print(i)


#sum of all numbers using while-loop

a=1
sum=0
while(a<=5):
    sum+=a
    print(a)
    a=a+1
print("\t SUM:",sum)



#sum using all numbers using for=loop
sum=0
for a in range(1,5+1):
    sum+=a
    print(a)
print("\t Sum:",sum)


#find even numbers using while loop

a=1
sum=0
while(a<=100):
    if(a%2==0):
        sum+=a
        print(a)
    a=a+1
print("\t Sum of even numbers:",sum)


#find even numbers using for-loop

sum=0
for a in range(1,100+1):
    if(a%2==0):
        sum+=a
        print(a)
    a=a+1
print("\t The sum of even numbes:",sum)


#find odd numbers using while-loop

a=1
sum=0
while(a<=100):
    if(a%2!=0):
        sum+=a
        print(a)
    a=a+1
print("\t Sum of odd numbers:",sum)


#find odd numbers using for-loop

sum=0
for a in range(1,100+1):
    if(a%2!=0):
        sum+=a
        print(a)
    a=a+1
print("\t Sum of ODD numbers:",sum)



#print table using while

a=1
b=int(input("Enter a number for table:"))
while(a<=10):
    print(b,"*",a,"=",b*a)
    a=a+1



#print table using for loop
b=int(input("Enter number:"))
for a in range(1,10+1):
    print(b,"*",a,"=",b*a)



#to print 1 to 20 tables (for loop)
for i in range(1,11):
    for j in range(1,21):
        print(i*j,end="\t")

    print("\r")


#to print star pattern
for i in range(0,6):
    for j in range(0,i+1):
        print("*",end="")
    print()

row=int(input("Enter number of row:"))
for i in range (row+1,0,-1):
    for j in range(0,i):
        print(i,end="")
    print()


for i in range(0,6):
    for j in range(6-i-1):
        print(end=" ")
    for j in range(i+1):
        print(i,end=" ")
    print("\r")'''


row=int(input("enter number of row:"))
for i in range(row+1,0,-1):
    for j in range(6-i-1):
        print(end=" ")
    for j in range(1,i):
        print("*",end=" ")
    print("\r")

