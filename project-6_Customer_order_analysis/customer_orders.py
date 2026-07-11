import pandas as pd
df=pd.read_csv("customer_orders.csv")
df=df.drop_duplicates()
df['Revenue']=df['Quantity']*df['Price']
df['Discount_Amount']=df['Revenue']*df['Discount']/100
df['Final_Revenue']=df['Revenue']-df['Discount_Amount']
total_revenue=df['Final_Revenue'].sum()
average=df['Final_Revenue'].mean()
customer=df.groupby('Customer')['Final_Revenue'].sum()
highest_spend=customer.nlargest(1)
product=df.groupby('Product')['Final_Revenue'].sum()
product_sale=product.nlargest(1)
city=df.groupby('City')['Final_Revenue'].sum()
category=df.groupby('Category')['Final_Revenue'].sum()
payment=df['Payment_Method'].value_counts()
highest_payment=payment.max()
payment_method=payment[payment==highest_payment]
customer_sales=customer.nlargest(5)
product_quantity=df.groupby('Product')['Quantity'].sum()
product_sales=product_quantity.nlargest(5)
highest_discount=df['Discount_Amount'].idxmax()
highest_discount_row=df.loc[highest_discount]
total_average=customer.mean().round(2)
above_average_spender=total_average<customer
above_average_spenders=customer[above_average_spender]
below_average_spender=total_average>customer
below_average_spenders=customer[below_average_spender]
print(df)
print("\n========== MANAGEMENT SUMMARY ==========\n")
print(f"\n1)Total Revenue after discount: {total_revenue}")
print(f"\n2)Average Revenue after discount: {average}")
print(f"\n3)Highest spender:\n{highest_spend}")
print(f"\n4)Highest product revenue:\n{product_sale}")
print(f"\n5)City revenue:\n{city}")
print(f"\n6)Category revenue:\n{category}")
print(f"\n7)Most pereferred payment method = \n{payment_method}")
print(f"\n8)Top 5 customers:\n{customer_sales}")
print(f"\n9)Top 5 products:\n{product_sales}")
print(f"\n10)Customer with the highest discount amount:\n{highest_discount_row}")
print(f"\n11)Above average spender:\n{above_average_spenders}")
print(f"\n12)Below average spender:\n{below_average_spenders}")
df.to_csv("Cleaned_customer_orders.csv",index=False)