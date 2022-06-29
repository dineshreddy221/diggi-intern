# imported required libraries
import pandas as pd
import numpy as np

# df = pd.read_csv(r"C:\Users\Lakshman\Downloads\ML & DL\dataset\Hero Motocorp.csv")
# df = pd.read_csv(r"C:\Users\Lakshman\Downloads\ML & DL\Machine Learning\Loan prediction\train_ctrUa4K.csv")
df = pd.read_csv(r"E:\Datascience projects\Web_Scraping\real_estate_data.csv")
print(df.head())

# df['Deliverable Quantity'].fillna(float(df['Deliverable Quantity'].median()), inplace=True)

# filling null values in traded quantity
# df['% Deli. Qty to Traded Qty'].fillna(df['% Deli. Qty to Traded Qty'].median(), inplace=True)
print(df.isnull().sum())

df['companies'] = df['companies'].apply(lambda x: x.replace("\n", "") if "\n" in x else x)
df['locations'] = df['locations'].apply(lambda x: x.replace("\n", "") if "\n" in x else x)
df['published_by'] = df['published_by'].apply(lambda x: x.replace("\n", "") if "\n" in x else x)

# price feature seection

# print(df['prices'])
