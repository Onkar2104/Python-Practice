a=input("Enter value of a:")

try:
    a = int(a)
    if(a>10):
        print("A is Greater than B")
         
except Exception as e:
    print(e)