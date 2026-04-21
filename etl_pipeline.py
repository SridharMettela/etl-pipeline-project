import pandas as pd

# Extract
df = pd.read_csv("data.csv")

# Transform
df['Total'] = df['Quantity'] * df['Price']

# Data Cleaning
df.dropna(inplace=True)

# Aggregation
summary = df.groupby('Product')['Total'].sum().reset_index()

# Load
df.to_csv("output.csv", index=False)
summary.to_csv("summary.csv", index=False)

print("ETL Process Completed Successfully")
