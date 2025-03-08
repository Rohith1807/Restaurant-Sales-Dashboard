# Restaurant-Sales-Dashboard
It is an **interactive dashboard** created using **PowerBI**. The dashboard analyses the **Sales**, reviews the **Menu performance** and gives insights about its **customers** for a restaurant business. The data is generated through Mockaroo and cleaned using **Python**.
# Features
- **Sales analysis**- Visualizes monthly sales trends and provides an overview of total orders, sales and profits
- **Menu performance**- Throws light on top and least selling items, analyses the profit margins of the menu items and sales based on categories
- **Customer’s insights**- Gives insights on total customers, Average of order values and customer’s lifetime values. Also highlights its top customers and their spendings.
# Dataset & Data cleaning
- **Source**- Mockaroo-generated data
- **Cleaning**- Python(Pandas,Numpy)
- **Data Files**- <a href=https://github.com/Rohith1807/Restaurant-Sales-Dashboard/tree/main/data>Data Folder</a>
# Dashboard Insights & Screenshots
- **Sales Analysis**-
	![sales_analysis](https://github.com/user-attachments/assets/979c64fa-c1ec-4c91-9f1a-acf53cce405a)
  - Added **Dropdown slicer** to select the **order types(dine-in, takeaway, delivery) and payment method(cash, card, online).**
  - **Card Titles** showing the **Total Orders, Sales, and Profits.**
  - Analyses **monthly sales trends** for the year 2023 & 2024 illustrated using the **Line graphs.**
  - **Category wise Sales** depicted in the **Piechart**
  - Useful in knowing the **overall performance of the restaurant.**

- **Menu Performance**
   ![menu_performance](https://github.com/user-attachments/assets/b4bab89f-65c5-44bc-83bd-84746f254c3b)
  - Shows the **Top 5 selling menu items** in the **Stacked bar chart** with its total sale value.
  - **Profit Margins** of the menu items.
  - Sales based on Category presented in **Piechart**
  - Displays the **Least selling** menu item
  - Helps in taking decisions whether to continue, improve and discontinue the menu items.
 
- **Customer's Insights**
  ![customers_insights](https://github.com/user-attachments/assets/76951cb6-f72a-48a7-8233-7a49ff1e10f9)
  - **Card Titles** displaying the **Total Customers, Average Order Value and Average Life-time spending** of the restaurant.
  - Helps in identifying the **top customers** of the restaurant and their contributions to the restaurant.
  - **Ability to analyse their customers based on the order types.**
  - Helpful for providing recognisition and adding value for thier top and regular customers.

- Overall the dashboard helps in analysing the performance of the restaurant and taking necessary actions for thier future sales, value thier customers and improvements on menu items.

# Technologies used
- **PowerBI**- For data visualization and analysis.
- **Python(Pandas,Numpy)**- Data cleaning, data manipulation and data analysis
- **CSV**- Dataset format

# **🚀 How to Use This Project?**  

**1️⃣ Clone the Repository**:

First, download the project files to your local machine:  
```bash
git clone https://github.com/Rohith1807/Restaurant-Sales-Dashboard.git
cd Restaurant-Sales-Dashboard
```
2️⃣ Explore the screenshots in the `screenshots/` folder to view the dashboard.

3️⃣ Access the raw and cleaned data in the `data/` folder.

4️⃣ Run the data cleaning script in the `scripts/` folder to understand the data preparation process.

5️⃣ **Create a Power BI Report**:

- Open Power BI Desktop.
- Click "Get Data" → "Text/CSV" and import the `merged_sales_menu_customers.csv` file.
- Perform any transformations (if needed) using Power Query.
- Use Power BI visuals (bar charts, slicers, KPIs) to create the dashboard.

# Data Preparation
The data used in this dashboard was generated using `Mockaroo`, a random data generator. The raw data was then cleaned and processed using Python to ensure consistency and accuracy.

**Steps Performed During Data Cleaning:**
- **Merging Data**: Combined `sales`, `menu`, and `customers` tables into a single dataset.
- **Date Conversion**: Converted the `order_date` column to a datetime format.
- **Total Price Calculation**: Calculated the `total_price` for each order by multiplying the price and quantity.
- **Data Validation**: Ensured data consistency (e.g., no negative sales values).

## Files Included:
**Raw Data**: The original data generated from Mockaroo is available in the `data/` folder:
- `sales.csv`
- `menu.csv`
- `customers.csv`

**Cleaned Data**: The processed and cleaned CSV file `(merged_sales_menu_customers.csv)` is available in the `data/` folder.

**Cleaning Code**: The Python script used for data cleaning is available in the `scripts/` folder.
## How to Run the Cleaning Code:
- Install the required Python libraries:
```bash
pip install pandas numpy
```
- Run the Python script:
```bash
python scripts/
```
    

