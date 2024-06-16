import pandas as pd

# Sample data
data = {
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles'],
    'Category': ['A', 'B', 'A', 'B'],
    'Sales': [100, 200, 150, 250]
}
data_frame = pd.DataFrame(data)
data_frame.set_index(['Date', 'City'], inplace=True)
print("DataFrame with Multi-Level Index:\n", data_frame)

pivoted_df = data_frame.reset_index().pivot(index='Date', columns='City', values='Sales')
print("\nPivoted DataFrame:\n", pivoted_df)
