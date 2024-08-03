import matplotlib.pyplot as plt

plt.style.use("ggplot")

price_x = ["1", "5", "10", "15", "50"]
quantity_y = [100, 500, 1000, 1500, 5000]

plt.plot(price_x, quantity_y, color="b")

plt.xlabel("Price")
plt.ylabel("Quantity")
plt.grid("True")

plt.legend()
plt.show()