from tkinter import *

x = Tk()
# x.geometry("300*300")
x.title("Welcome");
frame = Frame(x, width=500, height=300);

l=Label(x,text='Addition')
l.place(x=80,y=10)

l1=Label(x,text='no1')
l1.place(x=20,y=50)
t1=Entry(x)
t1.place(x=60,y=50)

l2=Label(x,text='no2')
l2.place(x=20,y=80)
t2=Entry(x)
t2.place(x=60,y=80)

t3=Entry(x,text='Display')
t3.place(x=60,y=110)
# t3=Entry(x,width=10)

# t3.place(x=100,y=550)

def Insert():
    no1 = int(t1.get())
    no2 = int(t2.get())

    res = no1 + no2
    t3.insert(END, str(res))

b1=Button(x, text="ADD", command=Insert)
b1.place(x=80, y=170)
frame.pack()
x.mainloop()