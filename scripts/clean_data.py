import pandas as pd
import numpy as np

# Load the data
sales = pd.read_csv('data/sales.csv')
menu = pd.read_csv('data/menu.csv')
customers = pd.read_csv('data/customers.csv')
promotions = pd.read_csv('data/promotions.csv')

# Function to clean data
def clean_data(df, table_name):
    print(f"Cleaning {table_name} table...")
    
    # Check for missing values
    print(f"Missing values in {table_name} table:\n", df.isnull().sum())
    
    # Drop rows with missing values in critical columns
    if table_name == 'sales':
        df.dropna(subset=['order_date', 'customer_id', 'menu_item_id', 'quantity'], inplace=True)
    elif table_name == 'menu':
        df.dropna(subset=['menu_item_id', 'item_name', 'price', 'cost'], inplace=True)
    elif table_name == 'customers':
        df.dropna(subset=['customer_id', 'name'], inplace=True)
    elif table_name == 'promotions':
        df.dropna(subset=['promotion_id', 'promotion_type', 'start_date', 'end_date'], inplace=True)
    
    # Check for duplicates
    print(f"Duplicate rows in {table_name} table:", df.duplicated().sum())
    df.drop_duplicates(inplace=True)
    
    # Ensure correct data types
    if table_name == 'sales':
        df['order_date'] = pd.to_datetime(df['order_date'], errors='coerce')
        df['quantity'] = pd.to_numeric(df['quantity'], errors='coerce')
    elif table_name == 'menu':
        df['price'] = pd.to_numeric(df['price'], errors='coerce')
        df['cost'] = pd.to_numeric(df['cost'], errors='coerce')
    elif table_name == 'promotions':
        df['start_date'] = pd.to_datetime(df['start_date'], errors='coerce')
        df['end_date'] = pd.to_datetime(df['end_date'], errors='coerce')
        df['discount_percentage'] = pd.to_numeric(df['discount_percentage'], errors='coerce')
    
    # Handle invalid data
    if table_name == 'menu':
        df = df[(df['price'] > 0) & (df['cost'] > 0)]  # Ensure positive prices and costs
    elif table_name == 'promotions':
        # Fix invalid date ranges (swap start_date and end_date if necessary)
        df['start_date'], df['end_date'] = np.where(
            df['start_date'] > df['end_date'],
            [df['end_date'], df['start_date']],
            [df['start_date'], df['end_date']]
        )
    
    print(f"{table_name} table cleaned successfully!\n")
    return df

# Clean each table
sales = clean_data(sales, 'sales')
menu = clean_data(menu, 'menu')
customers = clean_data(customers, 'customers')
promotions = clean_data(promotions, 'promotions')

# Verify data consistency
# Ensure menu_item_id in Sales matches menu_item_id in Menu
mismatched_menu_items = sales[~sales['menu_item_id'].isin(menu['menu_item_id'])]
print("Rows with mismatched menu_item_id:\n", mismatched_menu_items)
sales = sales[sales['menu_item_id'].isin(menu['menu_item_id'])]

# Ensure customer_id in Sales matches customer_id in Customers
mismatched_customers = sales[~sales['customer_id'].isin(customers['customer_id'])]
print("Rows with mismatched customer_id:\n", mismatched_customers)
sales = sales[sales['customer_id'].isin(customers['customer_id'])]

# Step 1: Merge Sales and Menu tables to get the price of each menu item
merged_data = pd.merge(sales, menu, on='menu_item_id')

# Step 2: Calculate the total_price for each order
merged_data['total_price'] = merged_data['price'] * merged_data['quantity']

# Step 3: Update the total_price column in the sales table
# Create a mapping of order_id to the new total_price
total_price_mapping = merged_data.set_index('order_id')['total_price'].to_dict()

# Update the sales table using the mapping
sales['total_price'] = sales['order_id'].map(total_price_mapping)

# Save cleaned and updated data
sales.to_csv('data/sales_cleaned.csv', index=False)
menu.to_csv('data/menu_cleaned.csv', index=False)
customers.to_csv('data/customers_cleaned.csv', index=False)
promotions.to_csv('data/promotions_cleaned.csv', index=False)

print("All tables cleaned, updated, and saved successfully!")