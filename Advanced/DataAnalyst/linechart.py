import matplotlib.pyplot as plt

plt.xkcd()
# plt.style.use("fivethirtyeight")
# plt.style.use("ggplot")

designation_x = ["MD", "Developer", "Programmer", "Assistance"]
salary_y = [50000, 45000, 30000, 25000]

plt.plot(designation_x, salary_y, color="b", label="All Developers")

sal_y=[75000,55000,35000,30000]
plt.plot(designation_x, sal_y, color='k', linestyle='--', linewidth=3, label="Python Developers")

plt.xlabel("Job-title")
plt.ylabel("Salary")
plt.grid("True")

plt.legend()
plt.savefig("linechart2.png")
plt.show()