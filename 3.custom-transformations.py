import pandas as pd

# Sample data
data = {
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles'],
    'Category': ['A', 'B', 'A', 'B'],
    'Sales': [100, 200, 150, 250]
}
data_frame = pd.DataFrame(data)


# Custom transformation function
def add_tax(sales):
    return sales * 1.05


# Applying the custom function
data_frame['Sales_with_Tax'] = data_frame['Sales'].transform(add_tax)
print("\nDataFrame with Custom Transformation:\n", data_frame)


