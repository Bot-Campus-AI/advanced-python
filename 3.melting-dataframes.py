import pandas as pd

# Sample pivoted data
pivoted_data = {
    'Date': ['2024-01-01', '2024-01-02'],
    'New York': [30, 32],
    'Los Angeles': [25, 28]
}
pivoted_df = pd.DataFrame(pivoted_data).set_index('Date')
print("Pivoted DataFrame:\n", pivoted_df)

# Melting the DataFrame
melted_df = pivoted_df.reset_index().melt(id_vars='Date', value_vars=['New York', 'Los Angeles'], var_name='City', value_name='Temperature')
print("\nMelted DataFrame:\n", melted_df)

