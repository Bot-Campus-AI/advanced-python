import pandas as pd

# Sample data
data = {
    'Name': ['Raj', 'Amit', 'Priya', 'Sara'],
    'Gender': ['Male', 'Male', 'Female', 'Female'],
    'Country': ['India', 'India', 'USA', 'UK']
}
data_frame = pd.DataFrame(data)

# Converting the 'Country' column to the 'category' dtype
data_frame['Country'] = data_frame['Country'].astype('category')

# Accessing categories and category codes
print("\nCategories in 'Country':", data_frame['Country'].cat.categories)
print("Category codes in 'Country':\n", data_frame['Country'].cat.codes)

# Adding a new category
data_frame['Country'] = data_frame['Country'].cat.add_categories(['Canada'])
print("\nCategories after adding 'Canada':", data_frame['Country'].cat.categories)

# Removing a category
data_frame['Country'] = data_frame['Country'].cat.remove_categories(['Canada'])
print("\nCategories after removing 'Canada':", data_frame['Country'].cat.categories)
