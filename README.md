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
- **PowerBI**- Dashboard creation
- **Python(Pandas,Numpy)**- Data cleaning
- **CSV**- Dataset format

In a **README.md** file on GitHub, you can format code blocks using triple backticks (```) for a clean and structured look. Here’s how you can format the **"How to Use This Project"** section with proper code blocks and styling:  

---

### **🚀 How to Use This Project?**  

#### **1️⃣ Clone the Repository**  
First, download the project files to your local machine:  
```bash
git clone https://github.com/Rohith1807/Restaurant-Sales-Dashboard.git
cd Restaurant-Sales-Dashboard
```

#### **2️⃣ Install Required Dependencies**  
Before running the script, install necessary Python libraries:  
```bash
pip install pandas numpy matplotlib seaborn
```

#### **3️⃣ Run the Data Cleaning Script**  
Execute the Python script to clean the raw dataset:  
```bash
python scripts/data_cleaning.py
```
This will generate a **cleaned CSV file** ready for use in Power BI.  

#### **4️⃣ Import Cleaned Data into Power BI**  
- Open **Power BI Desktop**.  
- Click **"Get Data" → "Text/CSV"** and select the cleaned dataset.  
- Perform any additional transformations using **Power Query**.  
- Use Power BI visuals to create **charts, KPIs, and reports**.  


 
   
    

