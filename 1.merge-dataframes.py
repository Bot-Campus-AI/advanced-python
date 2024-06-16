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

print("Left DataFrame:\n", left)
print("\nRight DataFrame:\n", right)

# Inner join
inner_merged = pd.merge(left, right, on='Key', how='inner')
print("\nInner Join:\n", inner_merged)

# Outer join
outer_merged = pd.merge(left, right, on='Key', how='outer')
print("\nOuter Join:\n", outer_merged)

# Left join
left_merged = pd.merge(left, right, on='Key', how='left')
print("\nLeft Join:\n", left_merged)

# Right join
right_merged = pd.merge(left, right, on='Key', how='right')
print("\nRight Join:\n", right_merged)
