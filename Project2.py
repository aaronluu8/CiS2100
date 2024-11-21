import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the CSV file generated in Project 1
sales_df = pd.read_csv("sales_data.csv")

# Display initial data information
print("Initial Data Info:")
print(sales_df.info())

# Convert 'Date' column to datetime format
sales_df['Date'] = pd.to_datetime(sales_df['Date'])

# Create new columns for 'Month' and 'Year'
sales_df['Month'] = sales_df['Date'].dt.to_period('M')
sales_df['Year'] = sales_df['Date'].dt.year

# Calculate total sales for each store
store_sales = sales_df.groupby('StoreID')['Price'].sum().reset_index()
store_sales.columns = ['StoreID', 'Total Sales']
print("\nTotal Sales per Store:")
print(store_sales)

# Calculate the number of unique orders per customer
customer_orders = sales_df.groupby('CustomerID')['OrderID'].nunique().reset_index()
customer_orders.columns = ['CustomerID', 'Number of Orders']
print("\nNumber of Orders per Customer:")
print(customer_orders)

# Determine the most popular products
popular_products = sales_df['Product Name'].value_counts().reset_index()
popular_products.columns = ['Product Name', 'Number of Sales']
print("\nMost Popular Products:")
print(popular_products)

# Analyze monthly sales trends
monthly_sales = sales_df.groupby('Month')['Price'].sum().reset_index()
monthly_sales.columns = ['Month', 'Total Sales']
print("\nMonthly Sales Trends:")
print(monthly_sales)

# Visualization

# Set up figure size
plt.figure(figsize=(10, 6))

# Bar plot for total sales per store
sns.barplot(x='StoreID', y='Total Sales', data=store_sales)
plt.title('Total Sales per Store')
plt.xlabel('Store ID')
plt.ylabel('Total Sales ($)')
plt.show()

# Set up figure size for monthly sales trend plot
plt.figure(figsize=(12, 6))

# Line plot for monthly sales trends
sns.lineplot(x='Month', y='Total Sales', data=monthly_sales, marker='o', color='b')
plt.title('Monthly Sales Trends')
plt.xlabel('Month')
plt.ylabel('Total Sales ($)')
plt.xticks(rotation=45)
plt.show()

# Set up figure size for popular products plot
plt.figure(figsize=(10, 6))

# Bar plot for most popular products
sns.barplot(x='Number of Sales', y='Product Name', data=popular_products, palette='viridis')
plt.title('Most Popular Products')
plt.xlabel('Number of Sales')
plt.ylabel('Product Name')
plt.show()
