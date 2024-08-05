import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
tips.head()
sns.countplot(y="time", data=tips)
plt.show()