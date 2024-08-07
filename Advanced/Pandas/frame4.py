import pandas

d1 = {"Name": ["Pankaj", "Ameya"], "ID": [1, 2]}
d2 = {"Name": ["David"], "ID": [3]}

df1 = pandas.DataFrame(d1, index=[1, 2])
df2 = pandas.DataFrame(d2, index=[3])

print('\n', df1)
print('\n', df2)

df3 = pandas.concat([df1, df2])

print('\n', df3)