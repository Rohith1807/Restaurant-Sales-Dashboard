import pandas as pd

# Load the cleaned data
sales = pd.read_csv('data/sales_cleaned.csv')
menu = pd.read_csv('data/menu_cleaned.csv')

# Step 1: Merge Sales and Menu tables to get the price of each menu item
merged_data = pd.merge(sales, menu, on='menu_item_id')

# Step 2: Calculate the total_price for each order
merged_data['total_price'] = merged_data['price'] * merged_data['quantity']

# Step 3: Update the total_price column in the sales table
# Create a mapping of order_id to the new total_price
total_price_mapping = merged_data.set_index('order_id')['total_price'].to_dict()

# Update the sales table using the mapping
sales['total_price'] = sales['order_id'].map(total_price_mapping)

# Save the updated sales table
sales.to_csv('data/sales_cleaned_updated.csv', index=False)

print("Total price updated in the sales table successfully!")
print("Sample of updated sales table:\n", sales.head())