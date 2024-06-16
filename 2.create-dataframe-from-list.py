import pandas as pd

# Creating a DataFrame from a list of lists
data = [
    ['Raj', 30, 'Delhi'],
    ['Amit', 25, 'Mumbai'],
    ['Priya', 35, 'Bangalore']
]
columns = ['Name', 'Age', 'City']
data_frame = pd.DataFrame(data, columns=columns)
print("DataFrame from list of lists:\n", data_frame)
