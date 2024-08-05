import numpy as np

x =np.array([1, 2, 3, 4])
print(x)

for i in x:
    print(i)

arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)

arr = np.array(["aa", "bb", "cc"], dtype='S')
print(arr)

# convert  float to integer using i
arr=np.array([1.1, 2.2, 3.3])
x = arr.astype('i')
print(x)
#covert float to integer using int
arr=np.array([1.1, 2.2, 3.3])
x = arr.astype(int)
print(x)

#covert integer to boolean
arr=np.array([1, 0, 3,-1])
x = arr.astype(bool)
print(x)