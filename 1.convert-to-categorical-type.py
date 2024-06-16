import pandas as pd

# Sample data
data = {
    'Name': ['Raj', 'Amit', 'Priya', 'Sara'],
    'Gender': ['Male', 'Male', 'Female', 'Female'],
    'Country': ['India', 'India', 'USA', 'UK']
}
data_frame = pd.DataFrame(data)
print("Original DataFrame:\n", data_frame)

# Converting 'Gender' and 'Country' columns to categorical type
data_frame['Gender'] = data_frame['Gender'].astype('category')
data_frame['Country'] = data_frame['Country'].astype('category')
print("\nDataFrame with Categorical Data:\n", data_frame)
print("\nData Types:\n", data_frame.dtypes)
