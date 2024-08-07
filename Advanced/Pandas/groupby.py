import pandas as pd
import numpy as np

data = {'Name': ['AA', 'BB', 'CC', 'DD'],
        'Percentage': [82, 98, 91, 87],
        'Course': ['B.Sc', 'B.Ed', 'M.Phill', 'BA']}
df = pd.DataFrame(data)

grouped = df.groupby('Course')
print(grouped['Percentage'].agg(np.mean))