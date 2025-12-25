import pandas as pd

#Loading Dataset
df = pd.read_csv('E:\\Econceptions assignment\\datasets\\sales_data.csv')

#Display - First 5 rows, Dataset shape, Column data types
print("First 5 rows: ")
print(df.head())

print("\n\nShape of the dataset: ")
print(df.shape)

print("\n\nColumn data types: ")
print(df.dtypes)

#Check for missing values
print("\n\nMissing values per column: ")
print(df.isnull().sum())
