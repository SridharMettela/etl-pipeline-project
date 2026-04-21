import pandas as pd

# Extract
df = pd.read_csv("data.csv")

# Transform
df['Total'] = df['Quantity'] * df['Price']

# Load
df.to_csv("output.csv", index=False)

print("ETL Process Completed")
