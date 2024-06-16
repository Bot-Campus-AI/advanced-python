import pandas as pd

# Sample data with missing values
data_with_nans = {
    'Date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04'],
    'Sales': [100, None, 150, None]
}
df_with_nans = pd.DataFrame(data_with_nans)

# Converting 'Sales' column to appropriate dtype
df_with_nans['Sales'] = pd.to_numeric(df_with_nans['Sales'])

# Converting 'Date' column to datetime dtype to ensure proper handling
df_with_nans['Date'] = pd.to_datetime(df_with_nans['Date'])

# Interpolating missing values
df_interpolated = df_with_nans.interpolate()
print("\nDataFrame with Interpolated Values:\n", df_interpolated)

# Filling missing values with the mean
df_filled_mean = df_with_nans.fillna(df_with_nans['Sales'].mean())
print("\nDataFrame with Mean Filled Values:\n", df_filled_mean)
