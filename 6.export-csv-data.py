import pandas as pd

# Creating a sample DataFrame
data = {
    'Name': ['Raj', 'Amit', 'Priya'],
    'Age': [30, 25, 35],
    'City': ['Delhi', 'Mumbai', 'Bangalore']
}
data_frame = pd.DataFrame(data)

# Writing to a CSV file
data_frame.to_csv('output.csv', index=False)
print("Data written to output.csv")
