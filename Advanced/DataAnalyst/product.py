import matplotlib.pyplot as plt
import numpy as np
Product = ("Laptop", "Mobile", "AC")
soldProduct = {
    'Quarterly Sold': (18.35, 18.43, 14.98),
    'Half yearly Sold': (38.79, 48.83, 47.50),
    'Yearly Sold': (189.95, 195.82, 217.19),
}
x = np.arange(len(Product))  # the label locations
width = 0.25  # the width of the bars
a = 0    # a is index no
fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in soldProduct.items():
    offset = width * a
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    a += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Length (mm)')
ax.set_title('Stock details in Shop')
ax.set_xticks(x + width, Product)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 300)

plt.show()