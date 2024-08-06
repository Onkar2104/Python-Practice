import numpy as np

# array of tuples
array1 = np.array([(0, 1), (2, 3)])

dataType = [('x', int), ('y', int)]

# dtype sets each tuple as an individual array element
array2 = np.array([(0, 1), (2, 3)], dtype = dataType)

# shape of array1
shape1 = np.shape(array1)

print('Shape of first array : ', shape1)

# shape of array2
shape2 = np.shape(array2)

print('Shape of second array : ', shape2)