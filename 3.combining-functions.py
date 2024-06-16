import pandas as pd

# Creating a time series with daily data
date_range = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')
time_series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=date_range)

# Calculating the rolling sum with a window of 3 days
rolling_sum = time_series.rolling(window=3).sum()
print("\nRolling Sum (3-day window):\n", rolling_sum)

# Calculating the expanding standard deviation
expanding_std = time_series.expanding().std()
print("\nExpanding Standard Deviation:\n", expanding_std)


