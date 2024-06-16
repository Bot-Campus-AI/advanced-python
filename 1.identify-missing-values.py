import pandas as pd

# Sample data with missing values
data = {
    'Name': ['Raj', 'Amit', 'Priya', None],
    'Age': [30, None, 35, 40],
    'City': ['Delhi', 'Mumbai', None, 'Bangalore']
}
data_frame = pd.DataFrame(data)
print("DataFrame with missing values:\n", data_frame)

# Identifying missing values
print("\nMissing values:\n", data_frame.isnull())
