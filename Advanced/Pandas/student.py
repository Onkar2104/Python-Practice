import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = './Advanced/Pandas/student.csv'

df = pd.read_csv(data)
pd.set_option('display.max.columns',None)
print(df.head())

# df.plot.line(y=['id', 'name', 'total_marks', 'per', 'grade'], figsize = (10,6))
df.plot.line(y=[ 'per'])
# plt.yticks(ticks=np.arange(len(df['grade'].unique())), labels=df['grade'].unique())

plt.show()

# import pandas as pd
# import numpy as np
# import matplotlib.pyplot as plt

# data = './Advanced/Pandas/student.csv'

# df = pd.read_csv(data)
# pd.set_option('display.max.columns', None)
# print(df.head())

# # Convert character values to numerical indices
# df['grade_index'] = pd.Categorical(df['grade']).codes

# # Plot using numerical indices
# df.plot.line(y='grade_index', figsize=(10, 6))

# # Set the tick labels to the original character values
# plt.yticks(ticks=np.arange(len(df['grade'].unique())), labels=df['grade'].unique())

# plt.show()
