import pandas as pd

# Sample data
data = {
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles'],
    'Category': ['A', 'B', 'A', 'B'],
    'Sales': [100, 200, 150, 250]
}
data_frame = pd.DataFrame(data)

# Grouping by multiple columns and applying aggregation functions
grouped = data_frame.reset_index().groupby(['Date', 'City']).agg({'Sales': ['sum', 'mean', 'max']})
print("\nGrouped DataFrame with Complex Aggregations:\n", grouped)

