#Dictionary keys are used to construct index
import pandas as pd
import numpy as np
data = {'a' : 11., 'b' : 1., 'c' : 25.33}
s = pd.Series(data,index=['b','c','d','a'])
print(s)