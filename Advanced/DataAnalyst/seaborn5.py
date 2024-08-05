# Importing seaborn library in program
import seaborn as sns
# Importing matplotlib library to show graph in output
import matplotlib.pyplot as plt

# Using set() function to set style
sns.set(style="ticks")
# Using dataset() function
ds = sns.load_dataset("anscombe")
# Showing results in the form of linear regression
sns.lmplot(x="x", y="y", data=ds)

plot = sns.lmplot(x="x", y="y", data=ds)
print(plot)
plt.show()  # using show() function