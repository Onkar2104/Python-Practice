import pandas as pd
import numpy as np

a = pd.Series(['Java', 'C', 'C++', np.nan])
print(a.map({'Java': 'Core'}))