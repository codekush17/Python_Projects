# tips-data-analysis.py

import pandas as pd

# Load dataset
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv"
df = pd.read_csv(url)

# Show basic structure
print("Top 5 rows:")
print(df.head())

# Total revenue per day
print("\nRevenue by day:")
print(df.groupby("day")["total_bill"].sum())

# Average tip by gender
print("\nAverage tip by gender:")
print(df.groupby("sex")["tip"].mean())

# Which day has the highest average total bill?
print("\nDay with highest average total bill:")
print(df.groupby("day")["total_bill"].mean().idxmax())
