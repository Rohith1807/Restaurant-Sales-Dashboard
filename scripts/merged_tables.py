import pandas as pd

# Load the data
sales = pd.read_csv('data/sales.csv')
menu = pd.read_csv('data/menu.csv')
customers = pd.read_csv('data/customers.csv')
promotions = pd.read_csv('data/promotions.csv')

# Convert date columns to datetime
sales['order_date'] = pd.to_datetime(sales['order_date'])
promotions['start_date'] = pd.to_datetime(promotions['start_date'])
promotions['end_date'] = pd.to_datetime(promotions['end_date'])

# Step 1: Merge sales and menu
merged_data = pd.merge(sales, menu, on='menu_item_id')

# Debugging: Print the first few rows after merging sales and menu
print("Merged Sales and Menu:")
print(merged_data[['order_id', 'menu_item_id', 'price', 'quantity']].head())

# Step 2: Calculate total_price
merged_data['total_price'] = merged_data['price'] * merged_data['quantity']

# Debugging: Print the first few rows after calculating total_price
print("\nAfter Calculating total_price:")
print(merged_data[['order_id', 'menu_item_id', 'price', 'quantity', 'total_price']].head())

# Step 3: Merge with customers
merged_data = pd.merge(merged_data, customers, on='customer_id')

# Step 4: Merge with promotions using a conditional join
# Perform a cross join first
merged_data = merged_data.merge(promotions, how='cross')

# Filter rows where order_date falls between start_date and end_date
merged_data = merged_data[
    (merged_data['order_date'] >= merged_data['start_date']) &
    (merged_data['order_date'] <= merged_data['end_date'])
]

# Step 5: Clean the discount_percentage column
# Replace NaN with 0 (no discount)
merged_data['discount_percentage'] = merged_data['discount_percentage'].fillna(0)

# Step 6: Add a flag for promotions
merged_data['is_promotion'] = merged_data['promotion_id'].notna()

# Step 7: Calculate final_total_price
def apply_promotion(row):
    total_price = row['total_price']
    discount_percentage = row['discount_percentage']
    
    # Ensure discount_percentage is numeric
    if pd.notna(discount_percentage) and isinstance(discount_percentage, (int, float)):
        total_price *= (1 - discount_percentage / 100)
    
    return total_price

merged_data['final_total_price'] = merged_data.apply(apply_promotion, axis=1)

# Debugging: Print the first few rows after calculating final_total_price
print("\nAfter Calculating final_total_price:")
print(merged_data[['order_id', 'total_price', 'discount_percentage', 'final_total_price']].head())

# Step 8: Include all sales (even those without promotions)
# Create a copy of the sales data with no promotions
non_promotion_sales = sales[~sales['order_id'].isin(merged_data['order_id'])]
non_promotion_sales = pd.merge(non_promotion_sales, menu, on='menu_item_id')
non_promotion_sales = pd.merge(non_promotion_sales, customers, on='customer_id')
non_promotion_sales['is_promotion'] = False
non_promotion_sales['final_total_price'] = non_promotion_sales['total_price']

# Combine promotional and non-promotional sales
final_data = pd.concat([merged_data, non_promotion_sales], ignore_index=True)

# Save the final data
final_data.to_csv('data/merged_sales_menu_customers_promotions.csv', index=False)

print("Merged CSV file created successfully!")