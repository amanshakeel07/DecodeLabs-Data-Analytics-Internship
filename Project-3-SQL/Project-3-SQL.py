import os
import pandas as pd
import sqlite3
# The filename of the dataset in your folder
DATASET_FILENAME = "Cleaned_Data_Project1.csv"
print("Initializing SQL Database Engine...")
# 1. Load your Cleaned Dataset
if os.path.exists(DATASET_FILENAME):
    df = pd.read_csv(DATASET_FILENAME)
    print(f"Successfully located and loaded: {DATASET_FILENAME}")
else:
    raise FileNotFoundError(f"Error: Could not find '{DATASET_FILENAME}' in this folder.")
# 2. Spin up an in-memory SQL Database Server
conn = sqlite3.connect(':memory:')
# 3. Write dataframe rows into a formal SQL relational table
df.to_sql('transactions', conn, index=False, if_exists='replace')
# 4. Helper function to cleanly display SQL outputs in your terminal
def execute_sql(query, title):
    print(f"QUERY: {title}")
    try:
        result = pd.read_sql_query(query, conn)
        if result.empty:
            print("[Empty Result Set - No records matched criteria]")
        else:
            print(result.to_string(index=False))
    except Exception as e:
        print(f"SQL Execution Error: {e}")
# Task 1: The Funnel (WHERE Clause Filtering)
query_task_1 = """
SELECT OrderID, Product, Quantity, UnitPrice, TotalPrice
FROM transactions
WHERE Product = 'Chair' AND Quantity >= 3
ORDER BY TotalPrice DESC
LIMIT 5;
"""
execute_sql(query_task_1, "Task 1 — High-Volume Bulk Chair Orders")
# Task 2: The Bucket & Aggregate (GROUP BY, SUM, COUNT, AVG)
query_task_2 = """
SELECT Product,
       COUNT(OrderID) AS TotalOrders,
       SUM(Quantity) AS TotalUnitsSold,
       ROUND(AVG(UnitPrice), 2) AS AvgUnitPrice,
       ROUND(SUM(TotalPrice), 2) AS GrossRevenue
FROM transactions
GROUP BY Product
ORDER BY GrossRevenue DESC;
"""
execute_sql(query_task_2, "Task 2 — Product Categorical Matrix")
# Task 3: Pattern & Search (LIKE Clause)
query_task_3 = """
SELECT OrderID, Product, Quantity, TotalPrice
FROM transactions
WHERE Product LIKE 'Phone%' OR Product LIKE '%Laptop%'
ORDER BY Quantity DESC
LIMIT 5;
"""
execute_sql(query_task_3, "Task 3 — Tech Hardware Substrings")
# Task 4: Advanced Slicing (HAVING Filter)
query_task_4 = """
SELECT Product, 
       SUM(Quantity) AS TotalVolume,
       ROUND(SUM(TotalPrice), 2) AS GroupRevenue
FROM transactions
GROUP BY Product
HAVING GroupRevenue > 160000
ORDER BY GroupRevenue DESC;
"""
execute_sql(query_task_4, "Task 4 — Elite Category Revenue Outliers")
# Close connection securely
conn.close()
print("\n🔒 SQL Database Engine connection securely closed.")