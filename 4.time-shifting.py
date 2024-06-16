import pandas as pd

# Creating a time series with daily data
date_range = pd.date_range(start='2024-01-01', end='2024-03-31', freq='D')
time_series = pd.Series(range(len(date_range)), index=date_range)

# Downsampling to monthly frequency and calculating the mean
monthly_resampled = time_series.resample('M').mean()

# Shifting data forward by one month
shifted_forward = monthly_resampled.shift(1)
print("\nTime Series Shifted Forward by One Month:\n", shifted_forward)

# Shifting data backward by one month
shifted_backward = monthly_resampled.shift(-1)
print("\nTime Series Shifted Backward by One Month:\n", shifted_backward)
