import pandas as pd

# Sample data
data = {
    'Name': ['Raj Kumar', 'Amit Sharma', 'Priya Singh', 'Sara Ali'],
    'Occupation': ['Data Scientist', 'Engineer', 'Doctor', 'Artist'],
    'Address': ['123 Elm St, Delhi', '456 Oak St, Mumbai', '789 Pine St, Bangalore', '101 Maple St, Pune']
}
data_frame = pd.DataFrame(data)

# Combining columns
data_frame['Name_Address'] = data_frame['Name'] + ', ' + data_frame['Address']

# Splitting addresses into multiple columns
address_split = data_frame['Address'].str.split(',', expand=True)
data_frame['Street'] = address_split[0]
data_frame['City'] = address_split[1]

print("\nDataFrame with Manipulated Text Data:\n", data_frame)



