import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve a single element
print(s['a'])  #value without index []

#retrieve multiple elements
print(s[['a','c','d']]) #value with index [[]]

print(s['b'])