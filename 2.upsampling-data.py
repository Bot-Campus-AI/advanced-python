import pandas as pd

# Creating a time series with daily data
date_range = pd.date_range(start='2024-01-01', end='2024-03-31', freq='D')
time_series = pd.Series(range(len(date_range)), index=date_range)

# Downsampling to monthly frequency and calculating the mean
monthly_resampled = time_series.resample('M').mean()

# Upsampling to daily frequency and forward filling missing values
daily_upsampled = monthly_resampled.resample('D').ffill()
print("\nUpsampled Time Series (Daily, Forward Fill):\n", daily_upsampled)
