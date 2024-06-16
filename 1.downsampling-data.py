import pandas as pd

# Creating a time series with daily data
date_range = pd.date_range(start='2024-01-01', end='2024-03-31', freq='D')
time_series = pd.Series(range(len(date_range)), index=date_range)
print("Original Time Series (Daily):\n", time_series)

# Downsampling to monthly frequency and calculating the mean
monthly_resampled = time_series.resample('M').mean()
print("\nResampled Time Series (Monthly Mean):\n", monthly_resampled)
