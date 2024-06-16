import pandas as pd

# Sample data with incorrect data types
data = {
    'Name': ['Raj', 'Amit', 'Priya'],
    'Age': ['30', '25', '35'],  # Age should be integers
    'City': ['Delhi', 'Mumbai', 'Bangalore']
}
data_frame = pd.DataFrame(data)
print("DataFrame with incorrect data types:\n", data_frame)

# Converting data types
data_frame['Age'] = data_frame['Age'].astype(int)
print("\nDataFrame after converting data types:\n", data_frame)
