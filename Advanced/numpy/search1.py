import numpy as np

arr = np.array([155, 365, 534, 723])

x = np.searchsorted(arr, [365, 5, 723])

print(x)