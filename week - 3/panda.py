import pandas as pd
import numpy as np

data = {"rolno": [1, 2, 3, 4, 5, 6, 7, 8],
        "names": ["ram", 3, "yoga", "mahesh", " ", "maheswari", "bhumi", "prasad"],
        "Gender": ["male", "male", np.nan, "male", "m", "female", "female", np.nan],
        "marks": [45, 56, "fiftyfive", 56, 35, 56, np.nan, 45]}

# creating a dataframe with data
df_1 = pd.DataFrame(data)
print(df_1.head(), end='\n')


df_1.set_index('rolno', inplace=True)
print("setting index as rolno: \n", df_1)

df_2 = pd.DataFrame({"class": [12, 12, 12, 12, np.nan, 12, 12, 12]})

# join class to df_1
df_1 = df_1.join(df_2)
print(df_1)
print("*"*25)

# checking for null values and data types
print(df_1.info())
print(df_1['names'].unique())

# filling null values
df_1['names'].replace(to_replace=3, value="dinesh", inplace=True)
df_1['names'] = df_1['names'].apply(lambda x: str(x.replace(" ", 'prasad')) if "" in x else str(x))
print(df_1['names'])

# Gender column filling null values
print(df_1['Gender'].unique())
df_1['Gender'].fillna(method='ffill', inplace=True)
df_1['Gender'].replace(to_replace='m', value='male', inplace=True)
print(df_1['Gender'])

# marks column
df_1['marks'].replace(to_replace='fiftyfive', value=55, inplace=True)
df_1['marks'].fillna(int(df_1['marks'].mean()), inplace=True)
print(df_1['marks'])

# class values
df_1['class'].fillna(method='ffill', inplace=True)
print(df_1.info())

# type changing
df_1['marks'] = df_1['marks'].astype(int)
df_1['class'] = df_1['class'].astype(int)
print(df_1.info())

# groupby on names
df_1_grp = df_1.groupby(by='names')
for marks, group in df_1_grp:
    print(marks)
    print(group)
    print()

df_1_grp_sum = df_1.groupby(['Gender']).sum()
print(df_1_grp_sum)

# group by and filter
df_1_fltr = df_1.groupby(['names', 'Gender']).filter(lambda x: len(x) >= 2)
print(df_1_fltr)

# statistical information
df_stats = df_1.groupby(['names'])
df_4 = df_stats['marks'].agg([np.mean, np.median, np.sum])
print(df_4)
