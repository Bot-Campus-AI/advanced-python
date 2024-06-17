import sqlite3

# Connecting to SQLite
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Deleting data
cursor.execute('''
DELETE FROM users
WHERE name = 'Amit Sharma'
''')

# Committing the changes and closing the connection
conn.commit()
conn.close()

print("Data deleted successfully.")
