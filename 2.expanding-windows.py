import pandas as pd

# Creating a time series with daily data
date_range = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')
time_series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=date_range)

# Calculating the expanding mean
expanding_mean = time_series.expanding().mean()
print("\nExpanding Mean:\n", expanding_mean)

