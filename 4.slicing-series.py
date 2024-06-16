import pandas as pd

# Creating a Series from a dictionary
data_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
data_series = pd.Series(data_dict)
print("Series from dictionary:\n", data_series)

# Slicing a Series using index labels
print("Slicing using index labels:\n", data_series['a':'c'])

# Slicing a Series using integer indices
print("Slicing using integer indices:\n", data_series[1:3])
