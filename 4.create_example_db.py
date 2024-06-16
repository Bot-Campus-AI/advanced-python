import sqlite3

# Establishing a connection to the database
conn = sqlite3.connect('example.db')

# Creating a cursor object
cursor = conn.cursor()

# Creating the example_table
cursor.execute('''
CREATE TABLE example_table (
    Name TEXT,
    Age INTEGER,
    City TEXT
)
''')

# Inserting data into the example_table
cursor.executemany('''
INSERT INTO example_table (Name, Age, City)
VALUES (?, ?, ?)
''', [
    ('Raj', 30, 'Delhi'),
    ('Amit', 25, 'Mumbai'),
    ('Priya', 35, 'Bangalore')
])

# Committing the transaction
conn.commit()

# Closing the connection
conn.close()

print("Database created and data inserted successfully.")
