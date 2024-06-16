import pandas as pd
import matplotlib.pyplot as plt

# Creating a time series with daily data
date_range = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')
time_series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=date_range)
print("Original Time Series:\n", time_series)

# Calculating rolling mean
rolling_mean = time_series.rolling(window=3).mean()

# Plotting original series and rolling mean
plt.figure()
time_series.plot(label='Original Series')
rolling_mean.plot(label='Rolling Mean (3-day window)')
plt.title('Time Series with Rolling Mean')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()




