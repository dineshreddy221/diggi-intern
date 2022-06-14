import pandas as pd
import numpy as np

data = {"names": [0, 1, 2, 3, 4, 5, 6, 7]}
# df = pd.Series(data)
# print(df[0][2])

df_1 = pd.DataFrame(data)
print(df_1.head())

df_2 = pd.date_range("20180501", periods=12)
print(df_2)

a = np.array([1, 2, 3, 4])
print(a*2)
