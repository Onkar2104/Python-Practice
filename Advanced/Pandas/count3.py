import pandas as pd
import numpy as np

info = pd.DataFrame({"Person":["Parker", "Smith", "William", "John"],
"Age": [27., 29, np.nan, 32] })

print(info)
print(info.count(axis='columns') )