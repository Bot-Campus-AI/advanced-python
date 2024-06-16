import pandas as pd

# Sample data with date strings
data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'Value': [10, 20, 30]
}
data_frame = pd.DataFrame(data)

# Converting the 'Date' column to datetime format
data_frame['Date'] = pd.to_datetime(data_frame['Date'])

# Adding 1 day to each date
data_frame['Date_plus_1'] = data_frame['Date'] + pd.Timedelta(days=1)
print("\nDataFrame with Dates Plus One Day:\n", data_frame)

# Calculating the difference between dates
date_diff = data_frame['Date'].diff()
print("\nDifference Between Dates:\n", date_diff)
