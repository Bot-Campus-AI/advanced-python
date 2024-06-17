import sqlite3

# Connecting to SQLite
conn = sqlite3.connect('example.db')

# Creating a cursor object to execute SQL commands
cursor = conn.cursor()

# Creating a table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    email TEXT UNIQUE
)
''')

# Committing the changes and closing the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
