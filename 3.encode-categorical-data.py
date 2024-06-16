import pandas as pd

# Sample data
data = {
    'Name': ['Raj', 'Amit', 'Priya', 'Sara'],
    'Gender': ['Male', 'Male', 'Female', 'Female'],
    'Country': ['India', 'India', 'USA', 'UK']
}
data_frame = pd.DataFrame(data)

# Encoding categorical data using get_dummies
encoded_df = pd.get_dummies(data_frame, columns=['Gender', 'Country'])
print("\nEncoded DataFrame with Dummy Variables:\n", encoded_df)


