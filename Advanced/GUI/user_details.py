from tkinter import *
import re
import tkinter.messagebox as MessageBox
import mysql.connector as db

x=Tk()
x.geometry("500x300")

l=Label(x, text="User Details")
l.place(x=20, y=30)

l1=Label(x, text="Enter your name: ")
l1.place(x=20, y=70)
t1=Entry()
t1.place(x=150, y=70)

l2=Label(x, text="Email Id: ")
l2.place(x=20, y=110)
t2=Entry()
t2.place(x=150, y=110)

l3=Label(x, text="Password: ")
l3.place(x=20, y=150)
t3=Entry()
t3.place(x=150, y=150)

l4=Label(x, text="Phone no.:")
l4.place(x=20, y=190)
t4=Entry()
t4.place(x=150, y=190)

l5=Label(x, text="Result")
l5.place(x=20, y=230)

def fun():
    user=t1.get()
    email=t2.get()
    ema =re.compile('[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}')
    if ema.match(email):
        # MessageBox.showinfo("alert, Valid Email")
        print(email)
    else:
        MessageBox.showinfo("Alert", "Invalid Email")

    pws=t3.get()
    phone=t4.get()
    number = re.compile('^[789]\d{9}$')
    if number.match(phone):
        print("Valid phone number")
        # MessageBox.showinfo("Alert" "Invalid Number")
    else:
        # print("Invalid phone number")
        MessageBox.showinfo("Alert", "Invalid Number")

    x=user+"  "+ email+ "  "+ pws+ "  " + " " + phone
    l5.config(text=x)

    if (user=="" or email=="" or pws=="" or phone==""):
        MessageBox.showinfo("ALERT","Please enter all fields")
    else:
        con=db.connect(host="localhost", user="root", password="", database="user_details")
        cursor = con.cursor()
        cursor.execute("Insert into user_details values('" + user + "', '" + email + "','" + pws + "', '" + phone +  "')")
        cursor.execute("commit")



b1=Button(x, text="Submit", command=fun)
b1.place(x=150, y=250)

x.mainloop()