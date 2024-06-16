import pandas as pd

# Sample data
data = {
    'A': [1, 2, 3, 4],
    'B': [10, 20, 30, 40]
}
data_frame = pd.DataFrame(data)

# Applying a function to each element
elementwise_square = data_frame.map(lambda x: x ** 2)
print("\nElement-wise Square of DataFrame:\n", elementwise_square)

# Applying a function to a Series
data_frame['A'] = data_frame['A'].map(lambda x: x * 2)
print("\nDataFrame after Applying map to Column 'A':\n", data_frame)


