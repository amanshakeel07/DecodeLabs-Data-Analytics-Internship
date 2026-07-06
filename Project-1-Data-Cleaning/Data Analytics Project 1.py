import pandas as pd
# Load the dataset
df = pd.read_csv(r'C:\Users\Lenovo\Downloads\Dataset for Data Analytics - Sheet1.csv')
# Look at the first 5 rows and column names
print("Show First 5 Rows Of Dataset")
print(df.head())
# Look at the data types and missing values summary
print("\nDataset Summary")
print(df.info())
# 1. Handle Missing Values
coupon_mode = df['CouponCode'].mode()[0]
df['CouponCode'] = df['CouponCode'].fillna(coupon_mode)
# 2. Handle Duplicates
df = df.drop_duplicates(subset=['OrderID'], keep='first')
# 3. Standardize Formats
df['Date'] = pd.to_datetime(df['Date']).dt.strftime('%Y-%m-%d')
df['Product'] = df['Product'].str.strip().str.title()
df['OrderStatus'] = df['OrderStatus'].str.strip().str.title()
df['UnitPrice'] = df['UnitPrice'].round(2)
df['TotalPrice'] = df['TotalPrice'].round(2)
# 4. Save your clean dataset!
df.to_csv('Cleaned_Data_Project1.csv', index=False)
print("Data successfully scrubbed and saved!")