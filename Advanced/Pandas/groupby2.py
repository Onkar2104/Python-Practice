import pandas as pd
import numpy as np

data = {'Name': ['AA', 'BB', 'CC', 'DD'],
        'Percentage': [82, 98, 91, 87],
        'Course': ['B.Sc', 'B.Ed', 'M.Phill', 'BA']}
df = pd.DataFrame(data)

grouped = df.groupby('Course')
print(df.groupby('Course').filter(lambda x: len(x) >= 1))