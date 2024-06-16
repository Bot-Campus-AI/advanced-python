import pandas as pd

# Sample data
data = {
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40]
}
data_frame = pd.DataFrame(data)
print("Original DataFrame:\n", data_frame)

# Applying a function to each column
column_sum = data_frame.apply(lambda x: x.sum())
print("\nSum of Each Column:\n", column_sum)

# Applying a function to each row
row_sum = data_frame.apply(lambda x: x.sum(), axis=1)
print("\nSum of Each Row:\n", row_sum)
