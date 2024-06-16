import pandas as pd

# Creating a time series with daily data
date_range = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')
time_series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=date_range)
print("Original Time Series:\n", time_series)

# Calculating the rolling mean with a window of 3 days
rolling_mean = time_series.rolling(window=3).mean()
print("\nRolling Mean (3-day window):\n", rolling_mean)
