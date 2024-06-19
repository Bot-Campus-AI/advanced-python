import pandas as pd
import numpy as np

# Creating a date range
date_range = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')
print("Date Range:\n", date_range)

# Creating a time series with random data
time_series = pd.Series(np.random.randn(len(date_range)), index=date_range)
print("\nTime Series:\n", time_series)

# Calculating a rolling mean with a window of 3 days
rolling_mean = time_series.rolling(window=3).mean()
print("\nRolling Mean (3-day window):\n", rolling_mean)

# Calculating an expanding mean
expanding_mean = time_series.expanding().mean()
print("\nExpanding Mean:\n", expanding_mean)