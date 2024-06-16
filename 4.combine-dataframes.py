import pandas as pd

# Sample data with missing values
df1 = pd.DataFrame({
    'A': [1, 2, None],
    'B': [None, 2, 3]
})

df2 = pd.DataFrame({
    'A': [4, None, 6],
    'B': [1, 2, None]
})

print("DataFrame 1:\n", df1)
print("\nDataFrame 2:\n", df2)

# Combining DataFrames with combine_first
combined_df = df1.combine_first(df2)
print("\nCombined DataFrame:\n", combined_df)
