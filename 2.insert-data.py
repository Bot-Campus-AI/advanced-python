import sqlite3

# Connecting to SQLite
conn = sqlite3.connect('example.db')
cursor = conn.cursor()

# Inserting data
cursor.execute('''
INSERT INTO users (name, age, email)
VALUES ('Raj Kumar', 30, 'raj.kumar@example.com')
''')

cursor.execute('''
INSERT INTO users (name, age, email)
VALUES ('Amit Sharma', 25, 'amit.sharma@example.com')
''')

# Committing the changes and closing the connection
conn.commit()
conn.close()

print("Data inserted successfully.")
