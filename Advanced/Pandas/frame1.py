import pandas as pd

data = {'product_name': ['computer', 'printer', 'tablet', 'monitor'],
        'price': [1200, 150, 300, 450]
        }

df = pd.DataFrame(data)

print(df)