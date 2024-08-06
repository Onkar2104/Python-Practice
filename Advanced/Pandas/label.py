import pandas as pd

a = [1, 7, 2]

x = pd.Series(a)

print(x[0])
print(x[1])
print(x[2])

x1 = pd.Series(a, index = ["aa", "bb", "cc"])

print(x1)