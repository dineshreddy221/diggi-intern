# imported required library
import pandas as pd

# loading the csv file to pandas dataframe
df = pd.read_csv(r"C:\Users\Lakshman\Downloads\production quaity\data_X.csv")

# checking the first ten rows with columns in a dataframe
print(df.head(10))

# checking for null values
print(df.isnull().sum())

# checking the count of values
print(df['T_data_2_3'].value_counts())

# checking for any object columns statistical description
print(df.describe(include=['object']))

# changing the object data type to datetime data type of date_time column
df['date_time'] = pd.to_datetime(df['date_time'])
print(df['date_time'])

