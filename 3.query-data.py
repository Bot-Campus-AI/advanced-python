import sqlite3

# Connecting to SQLite
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Querying data
cursor.execute('SELECT * FROM users')
rows = cursor.fetchall()

# Printing the queried data
for row in rows:
    print(row)

# Closing the connection
conn.close()
