import pandas as pd

# Sample data with date strings
data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'Value': [10, 20, 30]
}
data_frame = pd.DataFrame(data)

# Converting the 'Date' column to datetime format
data_frame['Date'] = pd.to_datetime(data_frame['Date'])

# Converting to a different time zone
data_frame['Date_UTC'] = data_frame['Date'].dt.tz_localize('UTC')
data_frame['Date_EST'] = data_frame['Date_UTC'].dt.tz_convert('US/Eastern')
print("\nDataFrame with Time Zones:\n", data_frame)
