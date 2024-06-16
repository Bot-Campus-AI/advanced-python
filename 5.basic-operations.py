import pandas as pd

# Creating a Series from a dictionary
data_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
data_series = pd.Series(data_dict)
print("Series from dictionary:\n", data_series)

# Performing element-wise operations
print("Series multiplied by 2:\n", data_series * 2)
print("Series added with 5:\n", data_series + 5)
