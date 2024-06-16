import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Raj', 'Amit', 'Priya'],
    'Age': [30, 25, 35],
    'City': ['Delhi', 'Mumbai', 'Bangalore']
}
data_frame = pd.DataFrame(data)

# Adding a new column
data_frame['Country'] = ['India', 'India', 'India']
print("DataFrame with new column:\n", data_frame)

# Removing a column
data_frame = data_frame.drop('Country', axis=1)
print("DataFrame after removing column:\n", data_frame)
