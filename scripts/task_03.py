import pandas as pd

df=pd.read_csv('E:\\Econceptions assignment\\datasets\\sales_data.csv')

#Creating new column for total price
df['total_price']=df['quantity']*df['unit_price']

#Converting order_date to datetime format
df['order_date'] = pd.to_datetime(df['order_date'])

#Creating new column for year and month
df['year_month']=df['order_date'].dt.to_period('M').astype(str)

print(df)