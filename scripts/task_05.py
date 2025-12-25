import pandas as pd

df=pd.read_csv('E:\\Econceptions assignment\\sales_data.csv')

#Total sales by region
df['total_price']=df['quantity']*df['unit_price']
sales_by_region=df.groupby('region')['total_price'].sum()
print("Total sales by region: ",sales_by_region)

#Average order value per customer
average_order_value=df.groupby('customer_id')['total_price'].mean()
print("\n\nAverage order value per customer: ",average_order_value)

#Orders with total price>1000
high_value_orders=df[df.total_price>1000]
print("\n\nOrders with total price > 1000: ",high_value_orders)
