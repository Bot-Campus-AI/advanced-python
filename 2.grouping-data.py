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

# Aggregating data within each group
mean_salary = grouped_data['Salary'].mean()
total_salary = grouped_data['Salary'].sum()

print("\nMean Salary by Name:\n", mean_salary)
print("\nTotal Salary by Name:\n", total_salary)
