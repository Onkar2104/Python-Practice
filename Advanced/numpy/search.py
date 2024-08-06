import numpy as np

arr = np.array([62, 33, 69, 80])
x = np.searchsorted(arr, 33,  sorter=None)
# y = np.searchsorted(arr, 33, side='right', sorter=None)
print(x)
# print(y)