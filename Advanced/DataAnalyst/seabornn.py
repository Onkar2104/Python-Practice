import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_theme(style="darkgrid")
tips = sns.load_dataset("tips")

sns.relplot(data=tips, x="total_bill", y="tip")

sns.relplot(data=tips, x="total_bill", y="tip", hue="smoker")


sns.relplot(
    data=tips,
    x="total_bill", y="tip", hue="smoker", style="smoker"
)

sns.pairplot(data = tips)

sns.relplot(
    data=tips,
    x="total_bill", y="tip", hue="smoker", style="time",
)

sns.relplot(
    data=tips, x="total_bill", y="tip", hue="size",
)

sns.relplot(
    data=tips,
    x="total_bill", y="tip",
    hue="size", palette="ch:r=-.5,l=.75"
)

#RGB tuples conversion to hex codes
# and a rich HTML representation.
# sns.relplot(
#     data=tips, x="total_bill", y="tip",
#     size="size", sizes=(15, 200)
# )

plt.show()
