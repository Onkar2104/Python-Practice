import seaborn as sns
import matplotlib.pyplot as plt
tips=sns.load_dataset("tips")
tips.head()
sns.countplot(y="sex",edgecolor=sns.color_palette("dark", 3),facecolor=(0,1,0,0),linewidth=2,data=tips)
plt.show()