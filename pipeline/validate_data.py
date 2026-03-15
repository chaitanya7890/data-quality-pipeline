import pandas as pd

# Read the raw dataset
df = pd.read_csv("../data/raw_sales_data.csv")

print("========== DATA VALIDATION REPORT ==========")

# Check for missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Check for invalid prices
print("\nInvalid Prices (price <= 0):")
invalid_prices = df[df["price"] <= 0]
print(invalid_prices)

# Check duplicate rows
print("\nDuplicate Records:")
duplicates = df[df.duplicated()]
print(duplicates)

# Total rows
print("\nTotal Records in Dataset:")
print(len(df))