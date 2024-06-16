import pandas as pd

# Sample data
data = {
    'Name': ['Raj', 'Amit', 'Priya', 'Amit', 'Raj', 'Priya'],
    'Age': [30, 25, 35, 28, 32, 38],
    'Salary': [70000, 80000, 75000, 85000, 72000, 77000]
}
data_frame = pd.DataFrame(data)
print("DataFrame:\n", data_frame)

# Applying aggregation functions
total_salary = data_frame['Salary'].sum()
average_age = data_frame['Age'].mean()
max_salary = data_frame['Salary'].max()

print("\nTotal Salary:", total_salary)
print("Average Age:", average_age)
print("Maximum Salary:", max_salary)
