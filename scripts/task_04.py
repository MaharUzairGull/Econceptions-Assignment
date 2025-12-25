import pandas as pd

df=pd.read_csv('E:\\Econceptions assignment\\datasets\\sales_data.csv')

#Calculating total sales amount
df['total_price']=df['quantity']*df['unit_price']

total_sales=df['total_price'].sum()
print("total sales amount: ",total_sales)

#Tope 3 products by total sales
top_products=df.groupby('product')['total_price'].sum().nlargest(3)
print("\n\nTope 3 products by total sales: ",top_products)

#Total sales per category
sales_per_category=df.groupby('category')['total_price'].sum()
print("\n\ntotal sales per category:",sales_per_category)

#Monthly sales trend
df['order_date'] = pd.to_datetime(df['order_date'])
df['year_month']=df['order_date'].dt.to_period('M').astype(str)
monthly_sales=df.groupby('year_month')['total_price'].sum()
print("\n\nMonthly sales trend ",monthly_sales)
