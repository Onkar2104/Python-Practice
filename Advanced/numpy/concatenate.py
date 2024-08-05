import numpy as np
x=np.array([[1,2],[3,4]])
y=np.array([[5,6]])
z=np.concatenate((x,y))
print(z)
#--numpy.concatenate() with axis=0 -----
a=np.array([[11,22],[33,44]])
b=np.array([[55,66]])
c=np.concatenate((a,b), axis=0)
print(c)
#--numpy.concatenate() with axis=1 -----
a=np.array([[11,22],[33,44]])
b=np.array([[55,66]])
c=np.concatenate((a,b.T), axis=1)
print(c)
#'.T' used to change the rows into columns and
# columns into rows.

#---numpy.concatenate() with axis=None---
a=np.array([[1,2],[3,4]])
b=np.array([[12,30]])
c=np.concatenate((a,b), axis=None)
print(c)