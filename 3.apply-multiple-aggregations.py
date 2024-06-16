import pandas as pd

# Sample data
data = {
    'Name': ['Raj', 'Amit', 'Priya', 'Amit', 'Raj', 'Priya'],
    'Age': [30, 25, 35, 28, 32, 38],
    'Salary': [70000, 80000, 75000, 85000, 72000, 77000]
}
data_frame = pd.DataFrame(data)

# Grouping data by Name
grouped_data = data_frame.groupby('Name')

# Applying multiple aggregation functions
agg_data = grouped_data['Salary'].agg(['mean', 'sum', 'max'])
print("\nMultiple Aggregations on Salary:\n", agg_data)
