import pandas as pd

# Sample data with duplicates
data = {
    'Name': ['Raj', 'Amit', 'Priya', 'Raj'],
    'Age': [30, 25, 35, 30],
    'City': ['Delhi', 'Mumbai', 'Bangalore', 'Delhi']
}
data_frame = pd.DataFrame(data)

# Removing duplicate rows
deduped_df = data_frame.drop_duplicates()
print("\nDataFrame after removing duplicates:\n", deduped_df)
