import pandas as pd

# Sample data
data = {
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02'],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles'],
    'Temperature': [30, 25, 32, 28]
}
data_frame = pd.DataFrame(data)
print("Original DataFrame:\n", data_frame)

# Pivoting the DataFrame
pivoted_df = data_frame.pivot(index='Date', columns='City', values='Temperature')
print("\nPivoted DataFrame:\n", pivoted_df)
