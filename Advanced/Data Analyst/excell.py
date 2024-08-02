# import pandas as pd
# from matplotlib import pyplot as plt

# plt.rcParams["figure.figsize"] = [7.00, 3.50]
# plt.rcParams["figure.autolayout"] = True

# columns = ["rollno", "name", "per"]
# df = pd.read_csv("Book1.csv", usecols=columns)

# print("Contents in csv file:", df)
# plt.plot(df.rollno, df.name, df.per)

# plt.show()

# import pandas as pd
# from matplotlib import pyplot as plt
# plt.rcParams["figure.figsize"] = [7.00, 3.50]
# plt.rcParams["figure.autolayout"] = True
# columns = ["rollno","name", "per"]
# df = pd.read_csv("Book1.csv", usecols=columns)
# print("Contents in csv file:", df)
# plt.plot(df.rollno, df.name, df.per)
# plt.grid("true")
# plt.show()

import pandas as pd
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = [7.00, 3.50]
plt.rcParams["figure.autolayout"] = True
columns = ["roll", "name", "per"]
df = pd.read_csv("abc.csv", usecols=columns)
print("Contents in csv file:", df)
plt.plot(df.roll, df.name, df.per)
# plt.grid("true")
plt.show()