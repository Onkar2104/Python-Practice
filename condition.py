#condition

#if
'''a=int(input("Enter Marks:"))
if(a>35):
    print("\t Pass")'''


#if-else ladder(elif)
'''if(a>=35 and a<=55):
    print("\t Third Class")

elif(a>=55 and a<80):
    print("\t Second Class")

elif(a>80 and a<=100):
    print("\t First Class")

elif not(a<100):
     print("\t Invalid")

else:
    print("\t Fail..!")'''


#nested if-else
'''a=int(input("Enter a:"))
b=int(input("ENter b:"))
if(a%5==0):
    print("\t Value is divisible")
    if(a%2==0):
        print("\t Value is divisible by 2")
    else:
        print("\t Not Divisible by 2")
else:
     print("\t Not divisible")'''




#Discount
amount=int(input("Enter Purchesed amount:"))
if(amount>=5000):
    print("\t You get 20 discount on your shopping")
    dis=amount*20/100
    # amount-=dis
    print("\t Discounted price is:",dis)

elif(amount>3000 and amount<5000):
    print("\t you get 10 discount on you shopping")
    dis=amount*10/100
    # amount-=dis
    print("\t The discounted amount is:",dis)
else:
    dis=amount*0/100
    print("\t Better luck next time.\n \t Discounted amount:",dis)
print("\t Net-Pay:",amount-dis)


#nothing
a=int(input("Enter a number:"))
if(a>70):
    print("The Number is greater than 70")
else:
    print(a)


a=float(input("Enter value of a:"))
b=float(input("Enter vlue of b:"))

if(a>b):
    print("\t A is greater than B")
elif(a<b):
    print("A is smaller than B")
else:
    print("A is equal to B")


day=int(input("Enter number between 1 to 7:"))

if (day==1):
    print("\t It is Sunday")
elif(day==2):
    print("\t It is Monday")
elif(day==3):
    print("\t It is Tuesday")
elif(day==4):
    print("\t It is Wednesday")
elif(day==5):
    print("\t It is Thursday")
elif(day==6):
    print("\t It is Friday")
elif day==7:
    print("It is Saturday")
else:
    print("Invalid..!")



a=int(input("Enter a:"))
if(a<0):
    print("\t The number is negative")
else:
    print("\t The number is not negative")




a=str(input("Enter an Alphabet:"))
b=str(input("Enter an Alphabet:"))

if(a==b):
    print("\t These two alphabets are same")
else:
    print("\t These two alphabet are different")