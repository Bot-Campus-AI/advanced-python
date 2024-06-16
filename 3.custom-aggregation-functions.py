import pandas as pd

# Creating a time series with daily data
date_range = pd.date_range(start='2024-01-01', end='2024-03-31', freq='D')
time_series = pd.Series(range(len(date_range)), index=date_range)

# Downsampling to monthly frequency and calculating the sum
monthly_sum = time_series.resample('M').sum()
print("\nResampled Time Series (Monthly Sum):\n", monthly_sum)
