import pandas as pd

# Creating a DataFrame from a dictionary
data = {
    'Name': ['Raj', 'Amit', 'Priya'],
    'Age': [30, 25, 35],
    'City': ['Delhi', 'Mumbai', 'Bangalore']
}
data_frame = pd.DataFrame(data)

# Filtering rows where Age is greater than 30
filtered_df = data_frame[data_frame['Age'] > 30]
print("Filtered DataFrame:\n", filtered_df)
