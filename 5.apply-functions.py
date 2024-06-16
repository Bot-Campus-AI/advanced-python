import pandas as pd

# Sample data
data = {
    'Name': ['Raj Kumar', 'Amit Sharma', 'Priya Singh', 'Sara Ali'],
    'Occupation': ['Data Scientist', 'Engineer', 'Doctor', 'Artist'],
    'Address': ['123 Elm St, Delhi', '456 Oak St, Mumbai', '789 Pine St, Bangalore', '101 Maple St, Pune']
}
data_frame = pd.DataFrame(data)


# Custom function to count words in a string
def word_count(text):
    return len(text.split())

# Applying the custom function to the 'Occupation' column
data_frame['Occupation Word Count'] = data_frame['Occupation'].apply(word_count)

print("\nDataFrame with Word Count in Occupation:\n", data_frame)




