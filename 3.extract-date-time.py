import pandas as pd

# Sample data with date strings
data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'Value': [10, 20, 30]
}
data_frame = pd.DataFrame(data)

# Converting the 'Date' column to datetime format
data_frame['Date'] = pd.to_datetime(data_frame['Date'])

# Extracting year, month, and day
data_frame['Year'] = data_frame['Date'].dt.year
data_frame['Month'] = data_frame['Date'].dt.month
data_frame['Day'] = data_frame['Date'].dt.day

print("\nDataFrame with Extracted Components:\n", data_frame)
