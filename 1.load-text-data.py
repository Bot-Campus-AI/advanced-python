import pandas as pd

# Sample data
data = {
    'Name': ['Raj Kumar', 'Amit Sharma', 'Priya Singh', 'Sara Ali'],
    'Occupation': ['Data Scientist', 'Engineer', 'Doctor', 'Artist'],
    'Address': ['123 Elm St, Delhi', '456 Oak St, Mumbai', '789 Pine St, Bangalore', '101 Maple St, Pune']
}
data_frame = pd.DataFrame(data)
print("Original DataFrame:\n", data_frame)
