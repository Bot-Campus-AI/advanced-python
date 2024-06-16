import pandas as pd

# Sample data with duplicates
data = {
    'Name': ['Raj', 'Amit', 'Priya', 'Raj'],
    'Age': [30, 25, 35, 30],
    'City': ['Delhi', 'Mumbai', 'Bangalore', 'Delhi']
}
data_frame = pd.DataFrame(data)
print("DataFrame with duplicates:\n", data_frame)

# Identifying duplicates
print("\nDuplicate rows:\n", data_frame.duplicated())
