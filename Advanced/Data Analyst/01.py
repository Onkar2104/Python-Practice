import matplotlib.pyplot as plt

x_axis = [1, 3, 5, 7]
y_axis = [0, 5, 3, 2]

plt.title("My Team")
plt.scatter(x_axis, y_axis, color="red", marker="*", label="My Chart type")

plt.xlabel("Single Point")
plt.ylabel("New point")

plt.grid(True)
plt.legend()
plt.show()