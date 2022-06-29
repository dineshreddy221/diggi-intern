# importing required library
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
import sklearn.preprocessing import OneHotEncoder


data = {"gender": ["male", "female", "male", "male", np.nan, 'female', np.nan, "male"],
        "math_score": [23, 26, 30, 32, 35, 25, 20, 45],
        "eligible": ['no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no', 'yes']}

df = pd.DataFrame(data)
print(df)



# log_reg = LogisticRegression()
