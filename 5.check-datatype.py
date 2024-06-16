import pandas as pd

# Sample data with duplicates
data = {
    'Name': ['Raj', 'Amit', 'Priya', 'Raj'],
    'Age': [30, 25, 35, 30],
    'City': ['Delhi', 'Mumbai', 'Bangalore', 'Delhi']
}
data_frame = pd.DataFrame(data)

# Checking data types
print("Data types in DataFrame:\n", data_frame.dtypes)
