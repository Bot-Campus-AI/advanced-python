import pandas as pd
import matplotlib.pyplot as plt

# Creating another time series
date_range = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')
time_series_1 = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], index=date_range)
time_series_2 = pd.Series([2, 3, 4, 5, 6, 7, 8, 9, 10, 11], index=date_range)

# Plotting multiple time series
plt.figure()
time_series_1.plot(label='Series 1')
time_series_2.plot(label='Series 2')
plt.title('Multiple Time Series Plot')
plt.xlabel('Date')
plt.ylabel('Value')
plt.legend()
plt.grid(True)
plt.show()


