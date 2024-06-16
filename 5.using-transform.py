import pandas as pd

# Sample data
data = {
    'Name': ['Raj', 'Amit', 'Priya', 'Amit', 'Raj', 'Priya'],
    'Age': [30, 25, 35, 28, 32, 38],
    'Salary': [70000, 80000, 75000, 85000, 72000, 77000]
}
data_frame = pd.DataFrame(data)

# Adding a column for mean salary by group
data_frame['Mean Salary by Name'] = data_frame.groupby('Name')['Salary'].transform('mean')
print("\nDataFrame with Mean Salary by Name:\n", data_frame)
