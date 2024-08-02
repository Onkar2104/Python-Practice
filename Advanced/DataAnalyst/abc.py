import pandas as pd
from matplotlib import pyplot as plt

plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True

columns = ["name", "per"]
df = pd.read_csv('./Advanced/DataAnalyst/abc.csv', usecols=columns)
print("Contents in csv file:", df)
plt.plot(df.name, df.per)

plt.show()