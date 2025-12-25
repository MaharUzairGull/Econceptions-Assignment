import pandas as pd

df=pd.read_csv('E:\\Econceptions assignment\\datasets\\sales_data.csv')\

#creating column for total price
df['total_price']=df['quantity']*df['unit_price']

#changing order_date to datetime format for month-year extraction
df['order_date']=pd.to_datetime(df['order_date'])
df['month_year']=df['order_date'].dt.to_period('M').astype(str)

#Category wise sales
category_sales=df.groupby('category')['total_price'].sum()
print("Category wise sales: ",category_sales)

#Saving category_sales into csv
category_sales.to_csv('E:\\Econceptions assignment\\datasets\\category_sales.csv')

#Saving monthly_sales into csv
monthly_sales=df.groupby('month_year')['total_price'].sum()
monthly_sales.to_csv('E:\\Econceptions assignment\\datasets\\monthly_sales.csv')