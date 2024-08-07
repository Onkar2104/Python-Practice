import pandas as pd

values_list = [[15, 2.5,100],
               [20, 4.5,100],
               [25, 5.2,100],
               [45, 5.8,100],
               [40, 6.3,100],
               [41, 6.4,100],
               [51, 2.3,100]]

df = pd.DataFrame(values_list, columns=['Prod_Rate', 'Discount', 'per'])

df = df.assign(interest=lambda x: (x['Prod_Rate'] * x['Discount'] * x['per']))

print(df)