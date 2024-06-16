import pandas as pd

# Sample data
data = {
    'Name': ['Raj Kumar', 'Amit Sharma', 'Priya Singh', 'Sara Ali'],
    'Occupation': ['Data Scientist', 'Engineer', 'Doctor', 'Artist'],
    'Address': ['123 Elm St, Delhi', '456 Oak St, Mumbai', '789 Pine St, Bangalore', '101 Maple St, Pune']
}
data_frame = pd.DataFrame(data)

# Extracting first names
data_frame['First Name'] = data_frame['Name'].str.split().str[0]

# Extracting cities from addresses
data_frame['City'] = data_frame['Address'].str.extract(r'(\bDelhi\b|\bMumbai\b|\bBangalore\b|\bPune\b)')

print("\nDataFrame with Extracted Information:\n", data_frame)


