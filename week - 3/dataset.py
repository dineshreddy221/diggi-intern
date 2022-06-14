# Importing required libraries
import pandas as pd
# import numpy as np

df = pd.read_csv(r"C:\Users\Lakshman\Downloads\ML & DL\dataset\Churn_Modelling.csv")
print(df.head())

# checking the shape of a dataset
print(df.shape)

# checking information
print(df.info())

# describe gives us descriptive statistical information for numerical variable
print(df.describe())

# describe for categorical variables
df_desc_cat = df.describe(include=['object'])
print(df_desc_cat)

# checking for null values
df_null = df.isnull().sum()
print(df_null)  # there are no null values in the dataset

# this gives us the unique values
print(df['Gender'].unique())

# finding the surname of male using geography as spain.
df_surname = df['Surname'][(df['Gender'] == 'Male') & (df['Geography'] == 'Spain')]
print(df_surname)
