import pandas as pd

# Creating a Series from a dictionary
data_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
data_series = pd.Series(data_dict)

# Creating a Series with missing values
data_with_nan = pd.Series([10, None, 20, None, 30])
print("Series with missing values:\n", data_with_nan)

# Checking for missing values
print("Is null:\n", data_with_nan.isnull())

# Filling missing values
filled_series = data_with_nan.fillna(0)
print("Filled missing values:\n", filled_series)
