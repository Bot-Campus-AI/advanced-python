import pandas as pd
import matplotlib.pyplot as plt

# Creating a time series with daily data
date_range = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')
time_series = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=date_range)
print("Original Time Series:\n", time_series)

# Plotting the time series
time_series.plot(title='Basic Time Series Plot')
plt.xlabel('Date')
plt.ylabel('Value')
plt.show()
