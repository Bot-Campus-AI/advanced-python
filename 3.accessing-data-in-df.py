import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Raj', 'Amit', 'Priya'],
    'Age': [30, 25, 35],
    'City': ['Delhi', 'Mumbai', 'Bangalore']
}
data_frame = pd.DataFrame(data)

# Accessing columns using bracket notation
print("Names column:\n", data_frame['Name'])

# Accessing columns using dot notation
print("Ages column:\n", data_frame.Age)
