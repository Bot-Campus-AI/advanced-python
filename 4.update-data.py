import sqlite3

# Connecting to SQLite
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Updating data
cursor.execute('''
UPDATE users
SET age = 31
WHERE name = 'Raj Kumar'
''')

# Committing the changes and closing the connection
conn.commit()
conn.close()

print("Data updated successfully.")
