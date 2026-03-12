import pandas as pd

# Load the dataset
# Ensure the CSV file is in the same directory
file_path = 'superstore_data.csv'
df = pd.read_csv(file_path)

# 1. Data Cleaning & Preprocessing
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Sales'] = pd.to_numeric(df['Sales'], errors='coerce')

# 2. Calculating High-Level KPIs
total_sales = df['Sales'].sum()
total_orders = df['Order ID'].nunique()

print(f"Total Sales: ${total_sales:,.2f}")
print(f"Total Orders: {total_orders}")

# 3. Sales by Category
category_sales = df.groupby('Category')['Sales'].sum().sort_values(ascending=False)
print("\nSales by Category:")
print(category_sales)

# 4. Sales by Region
region_sales = df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
print("\nSales by Region:")
print(region_sales)

# 5. Monthly Sales Trend
df['YearMonth'] = df['Order Date'].dt.to_period('M')
monthly_trend = df.groupby('YearMonth')['Sales'].sum()

# Exporting processed data for visualization
# monthly_trend.to_csv('monthly_sales_trend.csv')
