import pandas as pd
import numpy as np

df = pd.DataFrame({"A": [-5, 8, 12, None, 5, 3],
                   "B": [-1, None, 6, 4, None, 3],
                   "C":["sam", "haris", "alex", np.nan, "peter", "nathan"]})
                   
print(df)
print(df.count(axis=1))