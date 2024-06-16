import pandas as pd

# Sample data
data = {
    'Name': ['Raj', 'Amit', 'Priya', 'Amit', 'Raj', 'Priya'],
    'Age': [30, 25, 35, 28, 32, 38],
    'Salary': [70000, 80000, 75000, 85000, 72000, 77000]
}
data_frame = pd.DataFrame(data)

# Grouping data by Name and Age
multi_grouped_data = data_frame.groupby(['Name', 'Age'])

# Aggregating data within each group
multi_agg_data = multi_grouped_data['Salary'].sum()
print("\nTotal Salary by Name and Age:\n", multi_agg_data)
