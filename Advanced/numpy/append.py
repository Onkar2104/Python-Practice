import numpy as np

arr = np.array([[1, 2],[3, 4]])
arr1 = np.array([[5, 6],[7, 8]])
arr2 = np.append(arr, arr1, axis=0)
print(arr2)