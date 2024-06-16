import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Raj', 'Amit', 'Priya'],
    'Age': [30, 25, 35],
    'City': ['Delhi', 'Mumbai', 'Bangalore']
}
data_frame = pd.DataFrame(data)
print("DataFrame from dictionary:\n", data_frame)
