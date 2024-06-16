import pandas as pd

# Sample data
df1 = pd.DataFrame({
    'A': ['A0', 'A1', 'A2'],
    'B': ['B0', 'B1', 'B2']
})

df2 = pd.DataFrame({
    'A': ['A3', 'A4', 'A5'],
    'B': ['B3', 'B4', 'B5']
})

print("DataFrame 1:\n", df1)
print("\nDataFrame 2:\n", df2)

# Concatenating DataFrames vertically
vertical_concat = pd.concat([df1, df2], axis=0)
print("\nVertical Concatenation:\n", vertical_concat)

# Concatenating DataFrames horizontally
horizontal_concat = pd.concat([df1, df2], axis=1)
print("\nHorizontal Concatenation:\n", horizontal_concat)
