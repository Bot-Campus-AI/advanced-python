import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Raj', 'Amit', 'Priya'],
    'Age': [30, 25, 35],
    'City': ['Delhi', 'Mumbai', 'Bangalore']
}
data_frame = pd.DataFrame(data)

# Accessing rows using loc
print("First row using loc:\n", data_frame.loc[0])

# Accessing rows using iloc
print("Second row using iloc:\n", data_frame.iloc[1])
