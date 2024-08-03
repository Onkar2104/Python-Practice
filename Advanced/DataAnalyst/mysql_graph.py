import mysql.connector as db
import matplotlib.pyplot as plt

mydb = db.connect(host="localhost", user="root", password="", database="bitdb")
c=mydb.cursor()
c.execute("select * from studentinfo")
res=c.fetchall

Name = []
Percentage= []

for i in c:
    Name.append(i[1])
    Percentage.append(i[12])

print("Name of Student = ", Name)
print("Fetched Percentage= ", Percentage)

# Visualizing Data using Matplotlib
plt.bar(Name, Percentage)
plt.ylim(0, 100)
plt.xlabel("Name of Users")
plt.ylabel("Fetched Percentage")
plt.title("user Information")
plt.show()

