import pandas as pd
import numpy as np

a=pd.Series(['Java','C','C++',np.nan])
a.map({'Java':'Core'})
print(a.map(lambda x:'I like {}'.format(x)))