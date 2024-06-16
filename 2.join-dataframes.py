import pandas as pd

# Sample data
left = pd.DataFrame({
    'Key': ['A', 'B', 'C', 'D'],
    'Value1': [1, 2, 3, 4]
})

right = pd.DataFrame({
    'Key': ['B', 'C', 'D', 'E'],
    'Value2': [5, 6, 7, 8]
})

# Sample data with indices
left = left.set_index('Key')
right = right.set_index('Key')

print("Left DataFrame (with index):\n", left)
print("\nRight DataFrame (with index):\n", right)

# Joining DataFrames
joined_df = left.join(right, how='inner')
print("\nJoined DataFrame:\n", joined_df)
