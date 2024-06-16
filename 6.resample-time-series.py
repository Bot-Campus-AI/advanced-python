import pandas as pd

# Sample data with date strings
data = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03'],
    'Value': [10, 20, 30]
}
data_frame = pd.DataFrame(data)

# Creating a time series
time_series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=pd.date_range('2024-01-01', periods=10, freq='D'))
print("\nOriginal Time Series:\n", time_series)

# Resampling to 3-day frequency and calculating the mean
resampled = time_series.resample('3D').mean()
print("\nResampled Time Series (3-day mean):\n", resampled)
