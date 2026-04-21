import pandas as pd

# Step 1: Extract data from CSV file
df = pd.read_csv("data.csv")

# Step 2: Transform - create Total column
df['Total'] = df['Quantity'] * df['Price']

# Step 3: Data Cleaning - remove missing values
df.dropna(inplace=True)

# Step 4: Aggregation - summarize total sales per product
summary = df.groupby('Product')['Total'].sum().reset_index()

# Step 5: Load - save processed data
df.to_csv("output.csv", index=False)
summary.to_csv("summary.csv", index=False)

print("ETL Process Completed Successfully")
