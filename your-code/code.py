import pandas as pd

# 1. Create a DataFrame from a dictionary
data = {
    'Name': ['Ali', 'Fatima', 'Mohammed'],
    'Age': [25, 30, 22],
    'City': ['Cairo', 'Riyadh', 'Dubai']
}

df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)


print("\nDataFrame Information:")
print(df.info())

# 4. Descriptive statistics
print("\nDescriptive Statistics:")
print(df.describe())

# 5. Add a new column
df['Years of Experience'] = [2, 5, 1]
print("\nAfter Adding 'Years of Experience' Column:")
print(df)

# 6. Filter the data
filtered_df = df[df['Age'] > 25]
print("\nPeople older than 25:")
print(filtered_df)