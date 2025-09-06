import pandas as pd

# Load the CSV file
df = pd.read_csv("sample.csv")

# Drop the first column and the 'date' column
df = df.drop(df.columns[0], axis=1)   # drops the first column
df = df.drop("date", axis=1)          # drops the 'date' column

# Save the new CSV
df.to_csv("cleaned_sample.csv", index=False)

print("✅ Cleaned CSV saved as 'cleaned_sample.csv'")
