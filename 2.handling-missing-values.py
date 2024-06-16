import pandas as pd

# Sample data with missing values
data = {
    'Name': ['Raj', 'Amit', 'Priya', None],
    'Age': [30, None, 35, 40],
    'City': ['Delhi', 'Mumbai', None, 'Bangalore']
}
data_frame = pd.DataFrame(data)

# Dropping rows with missing values
dropped_df = data_frame.dropna()
print("\nDataFrame after dropping missing values:\n", dropped_df)

# Filling missing values with a specific value
filled_df = data_frame.fillna({'Name': 'Unknown', 'Age': 0, 'City': 'Unknown'})
print("\nDataFrame after filling missing values:\n", filled_df)
