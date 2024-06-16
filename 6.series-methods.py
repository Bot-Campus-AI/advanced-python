import pandas as pd

# Creating a Series from a dictionary
data_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
data_series = pd.Series(data_dict)
print("Series from dictionary:\n", data_series)

# Using built-in Series methods
print("Sum of Series:", data_series.sum())
print("Mean of Series:", data_series.mean())
print("Maximum value in Series:", data_series.max())
