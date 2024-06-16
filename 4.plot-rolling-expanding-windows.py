import pandas as pd
import matplotlib.pyplot as plt

# Creating a time series with daily data
date_range = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')
time_series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=date_range)

# Plotting the original time series
time_series.plot(title='Original Time Series', label='Original')
plt.legend()
plt.show()

# Calculating the rolling mean with a 3-day window
rolling_mean = time_series.rolling(window=3).mean()

# Plotting the rolling mean
rolling_mean.plot(title='Rolling Mean (3-day window)', label='Rolling Mean')
plt.legend()
plt.show()

# Calculating the expanding mean
expanding_mean = time_series.expanding().mean()

# Plotting the expanding mean
expanding_mean.plot(title='Expanding Mean', label='Expanding Mean')
plt.legend()
plt.show()
