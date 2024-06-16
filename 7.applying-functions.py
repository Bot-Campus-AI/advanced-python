import pandas as pd

# Sample data with missing values
data = {
    'Name': ['Raj', 'Amit', 'Priya', None],
    'Age': [30, None, 35, 40],
    'City': ['Delhi', 'Mumbai', None, 'Bangalore']
}
data_frame = pd.DataFrame(data)

# Applying a custom function to the Age column
data_frame['Age Group'] = data_frame['Age'].apply(lambda x: 'Adult' if x >= 18 else 'Minor')
print("\nDataFrame after applying function:\n", data_frame)
