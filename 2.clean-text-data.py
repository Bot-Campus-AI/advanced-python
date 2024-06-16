import pandas as pd

# Sample data
data = {
    'Name': ['Raj Kumar', 'Amit Sharma', 'Priya Singh', 'Sara Ali'],
    'Occupation': ['Data Scientist', 'Engineer', 'Doctor', 'Artist'],
    'Address': ['123 Elm St, Delhi', '456 Oak St, Mumbai', '789 Pine St, Bangalore', '101 Maple St, Pune']
}
data_frame = pd.DataFrame(data)

# Removing leading/trailing whitespace
data_frame['Name'] = data_frame['Name'].str.strip()

# Converting to lowercase
data_frame['Name'] = data_frame['Name'].str.lower()

# Removing special characters
data_frame['Address'] = data_frame['Address'].str.replace(r'\W', ' ', regex=True)

print("\nCleaned DataFrame:\n", data_frame)

