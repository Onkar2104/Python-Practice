import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

dataseturl='./Advanced/Pandas/Book1.csv'
df=pd.read_csv(dataseturl,parse_dates=['Date'],index_col='Date')
pd.set_option('display.max.columns',None)
print(df.head())

# df.plot(y='cprice',figsize=(9,6))

df.plot.line(y=['cprice','sprice','profit', 'loss'],figsize=(10,6))


# df.plot(y='cprice', figsize=(10,6), title='Annual Record', ylabel='Cost')
plt.show()