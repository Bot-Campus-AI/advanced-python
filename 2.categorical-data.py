import pandas as pd

# Sample data
data = {
    'Name': ['Raj', 'Amit', 'Priya', 'Sara'],
    'Gender': ['Male', 'Male', 'Female', 'Female'],
    'Country': ['India', 'India', 'USA', 'UK']
}
data_frame = pd.DataFrame(data)

# Creating a categorical column with specified categories and order
data_frame['Country'] = pd.Categorical(data_frame['Country'], categories=['India', 'USA', 'UK'], ordered=True)
print("\nDataFrame with Ordered Categorical Data:\n", data_frame)

