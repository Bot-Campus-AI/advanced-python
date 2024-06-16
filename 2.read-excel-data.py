# Install the openpyxl module before running this code
# pip install openpyxl

import pandas as pd

# Reading an Excel file
data_frame = pd.read_excel('example.xlsx', sheet_name='Sheet1')
print("DataFrame from Excel:\n", data_frame)
