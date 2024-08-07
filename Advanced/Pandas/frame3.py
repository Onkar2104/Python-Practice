import pandas as pd

df1 = pd.DataFrame({"a": [1, 2, 3, 4],
                    "b": [5, 6, 7, 8]})

df2 = pd.DataFrame({"a": [1, 2, 3],
                    "b": [5, 6, 7],
                    "c": [1, 5, 4]})

df3 = pd.concat([df1, df2], ignore_index=True)
print(df3)