import pandas as pd
import numpy as np

# Creating a date range
date_range = pd.date_range(start='2024-01-01', end='2024-01-10', freq='D')
print("Date Range:\n", date_range)

# Creating a time series with random data
time_series = pd.Series(np.random.randn(len(date_range)), index=date_range)
print("\nTime Series:\n", time_series)

# Indexing a specific date
print("\nValue on 2024-01-03:", time_series['2024-01-03'])

# Slicing a range of dates
print("\nTime Series from 2024-01-03 to 2024-01-07:\n", time_series['2024-01-03':'2024-01-07'])
