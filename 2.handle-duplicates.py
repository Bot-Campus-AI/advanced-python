import pandas as pd

# Sample data with duplicates
data = {
    'Date': ['2024-01-01', '2024-01-01', '2024-01-02', '2024-01-02', '2024-01-01'],
    'City': ['New York', 'Los Angeles', 'New York', 'Los Angeles', 'New York'],
    'Temperature': [30, 25, 32, 28, 33]
}
data_frame = pd.DataFrame(data)
print("Original DataFrame with Duplicates:\n", data_frame)

# Pivoting with pivot_table and handling duplicates
pivot_table_df = data_frame.pivot_table(index='Date', columns='City', values='Temperature', aggfunc='mean')
print("\nPivot Table DataFrame:\n", pivot_table_df)
