import pandas as pd
import numpy as np

values_list = [[1.5, 2.5, 10.0],
               [2.0, 4.5, 5.0],
               [2.5, 5.2, 8.0],
               [4.5, 5.8, 4.8],
               [4.0, 6.3, 70],
               [4.1, 6.4, 9.0],
               [5.1, 2.3, 11.1]]

df = pd.DataFrame(values_list, columns=['col_1', 'col_2', 'col_3'],
                  index=['a', 'b', 'c', 'd', 'e', 'f', 'g'])
print(df)

df = df.apply(lambda x: np.square(x) if x.name in ['b', 'f'] else x, axis=1)
print(df)

df_add = df.apply(lambda x: x + 10 if x.name in ['b', 'f'] else x, axis=1)
print(df_add)

total_col1=df["col_1"].sum()
total_col2=df["col_2"].sum()
total_col3=df["col_3"].sum()

print(f"Sum of col_1: {total_col1}")
print(f"total of col_2: {total_col2}")
print(f"total of col_3: {total_col3}")