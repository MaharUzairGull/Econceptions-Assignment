import pandas as pd
#Loading Dataset
df=pd.read_csv('E:\\Econceptions assignment\\datasets\\sales_data.csv')

#Handling missing values
df['quantity']=df['quantity'].fillna(1)

df=df.dropna(subset=['unit_price'])

#Converting order_date to datetime format
df['order_date']=pd.to_datetime(df['order_date'])

print(df)