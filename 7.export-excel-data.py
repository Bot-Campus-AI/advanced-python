import pandas as pd

# Reading an Excel file
data_frame = pd.read_excel('example.xlsx', sheet_name='Sheet1')
print("DataFrame from Excel:\n", data_frame)

# Writing to an Excel file
data_frame.to_excel('output.xlsx', sheet_name='Sheet1', index=False)
print("Data written to output.xlsx")
