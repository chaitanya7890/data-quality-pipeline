import pandas as pd

# Load dataset
df = pd.read_csv("../data/raw_sales_data.csv")

# Remove rows with missing values
df = df.dropna()

# Remove rows with invalid prices
df = df[df["price"] > 0]

# Save cleaned dataset
df.to_csv("../output/clean_sales_data.csv", index=False)

print("Clean dataset created successfully")