import pandas as pd

# Creating a Series from a dictionary
data_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
data_series = pd.Series(data_dict)
print("Series from dictionary:\n", data_series)

# Accessing elements using index labels
print("Element at index 'a':", data_series['a'])

# Accessing elements using integer indices
print("First element:", data_series.iloc[0])
