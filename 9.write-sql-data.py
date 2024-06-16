import pandas as pd
import sqlite3

# Establishing a connection to the database
conn = sqlite3.connect('example.db')

# Reading data from a SQL table
data_frame = pd.read_sql('SELECT * FROM example_table', conn)
print("DataFrame from SQL:\n", data_frame)

# Writing data to a SQL table
data_frame.to_sql('output_table', conn, if_exists='replace', index=False)
print("Data written to SQL table output_table")

# Closing the connection
conn.close()
