import pandas as pd

# Sample data with date strings
data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'Value': [10, 20, 30]
}
data_frame = pd.DataFrame(data)

# Converting date strings to datetime
data_frame['Date'] = pd.to_datetime(data_frame['Date'])
print("\nDataFrame with DateTime:\n", data_frame)
