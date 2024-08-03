import matplotlib.pyplot as plt
import numpy as nm

plt.style.use("fivethirtyeight")
stud_rollno_x = [1, 2, 3, 4]
x_indexes = nm.arange(len(stud_rollno_x))
width = 5

per_y = [99, 80, 90, 60]
plt.bar(x_indexes-width, per_y, color="red", label="III Years")

per1_y= [60, 40, 97, 70]
x_indexes=nm.arange(len(stud_rollno_x))
plt.bar(x_indexes, per1_y, color="yellow", label="II Year")

per2_y= [65, 90, 50, 70]
x_indexes=nm.arange(len(stud_rollno_x))
plt.bar(x_indexes + width, per2_y, color="pink", label="I Year")

plt.legend()
plt.xticks(ticks=x_indexes, labels=stud_rollno_x)
plt.title("Details of Student")
plt.xlabel("Roll No.")
plt.ylabel("Percentage")
plt.show()
