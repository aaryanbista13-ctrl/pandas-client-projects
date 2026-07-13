import pandas as pd
#---------------------------
#--------Load_Data----------
#-----------------------
df=pd.read_csv('ecommerce_orders.csv')
#---------------------------
# ---Removing Duplicates Rows---
#--------------------------
df=df.drop_duplicates()
#---------------------------------------
# ---------Delivered_Orders_Anlaysis------
#-----------------------------------------
df['Order_Value'] = df['Quantity'] * df['Price']
df['Discount_Amount'] = df['Order_Value'] * df['Discount'] / 100
df['Final_Revenue'] = df['Order_Value'] - df['Discount_Amount']
delivered=df[df['Order_Status']=='Delivered']
delivered_revenue=delivered['Final_Revenue'].sum()
avg_total_revenue=delivered['Final_Revenue'].mean().round(2)
highest_value_order=delivered.nlargest(1,'Final_Revenue')
lowest_value_order=delivered.nsmallest(1,'Final_Revenue')
top_5_valueorder=delivered.nlargest(5,'Final_Revenue')
city_revenue=delivered.groupby('City')['Final_Revenue'].sum()
category_revenue=delivered.groupby('Category')['Final_Revenue'].sum()
#-------------------------------
#-------Most_Payment_Used------------
#----------------------------------
payment=delivered['Payment_Method'].value_counts()
payment_max=payment.max()
payment_method=payment[payment==payment_max]
#-------------------------------
#-----------Most_Sold and Highest Spending---------------
#------------------------------------------
most_sold=delivered.groupby('Product')['Quantity'].sum()
most_sold_product=most_sold.nlargest(1)
top_5_spending=delivered.groupby('Customer')['Final_Revenue'].sum()
top_5_spendings=top_5_spending.nlargest(5)
#-------------------------------------
#------------Total_Discount---------
#-----------------------------------
total_discount_amount=delivered['Discount_Amount'].sum()
highest_discounted_customer=delivered.nlargest(1,'Discount_Amount')
#---------------------------------------
#---------Order_Status Percentage----------
#-------------------------------------
status=df['Order_Status'].value_counts()
delivered_percentage=round(status['Delivered']/len(df)*100,2)
cancelled_percentage=round(status['Cancelled']/len(df)*100,2)
returned_percentage=round(status['Returned']/len(df)*100,2)
#-----------------------------------
#-------Customer spending (Above and Below) Average revenue
#------------------------------------
up=delivered.groupby('Customer')['Final_Revenue'].sum()
up_avg=up.mean()
above=up_avg < up
above_avg_spending=up[above]
below=up_avg > up
below_avg_spending=up[below]
category=delivered['Category'].value_counts()
popular_category=category.nlargest(1)
print(df)
print("\n================Order_Analysis====================\n")
print(f"\n1)Total revenue after discount from delivered goods: {delivered_revenue}")
print(f"\n2)Avg revenue from delivered goods: {avg_total_revenue}")
print(f"\n3)Total revenue from highest value order:\n{highest_value_order}")
print(f"\n4)Total revenue from lowest value order:\n{lowest_value_order}")
print(f"\n5)Highest revenue from top 5 orders:\n{top_5_valueorder}")
print(f"\n6)City revenue:\n{city_revenue}")
print(f"\n7)Category revenue:\n{category_revenue}")
print(f"\n8)Most used Payment method:\n{payment_method}")
print(f"\n9)Most sold product:\n{most_sold_product}")
print(f"\n10)Top 5 customers after discount:\n{top_5_spendings}")
print(f"\n11)Total Discount given to all customers:{total_discount_amount}")
print(f"\n12)Order with Highest Discount:\n{highest_discounted_customer}")
print(f"\n13) Delivered percentage: {delivered_percentage}")
print(f"\n14) Cancelled percentage: {cancelled_percentage}")
print(f"\n15) Returned percentage: {returned_percentage}")
print(f"\n16) Customers spending above average revenue :\n{above_avg_spending}")
print(f"\n17) Customers spending below average revenue :\n{below_avg_spending}")
print(f"\n18) Most popular category:\n{popular_category}")
print("\n**************************************************************\n")
df.to_csv('cleaned_ecommerce_orders.csv',index=False)