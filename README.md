# Integrating Python with Databases - Introduction to SQL and Databases

## Overview
This tutorial explores how to integrate Python with databases, focusing on SQL and relational databases. Understanding these concepts is essential for managing and manipulating data effectively.

## Table of Contents
1. [Practical Applications of Integrating Python with Databases](#practical-applications-of-integrating-python-with-databases)
2. [Introduction to SQL and Databases](#introduction-to-sql-and-databases)
3. [Setting Up a Database](#setting-up-a-database)
4. [Inserting Data into the Database](#inserting-data-into-the-database)
5. [Querying Data from the Database](#querying-data-from-the-database)
6. [Updating and Deleting Data](#updating-and-deleting-data)
7. [About BotCampus AI](#about-botcampus-ai)

## Practical Applications of Integrating Python with Databases

### Practical Applications
Integrating Python with databases is crucial for building data-driven applications, performing data analysis, and managing large datasets. Knowing how to interact with databases allows you to store, retrieve, and manipulate data efficiently.

**Examples:**
- Web development
- Data analytics
- Machine learning

## Introduction to SQL and Databases

### What is SQL?
SQL, or Structured Query Language, is a standard programming language used for managing and manipulating relational databases. It allows you to perform various operations on the data stored in databases, such as querying, updating, and deleting records.

### What are Databases?
Databases are organized collections of data that can be easily accessed, managed, and updated. Relational databases, like MySQL, PostgreSQL, and SQLite, store data in tables consisting of rows and columns.

## Setting Up a Database

### Setting Up a Database
Let's start by setting up a SQLite database, which is a lightweight and easy-to-use database management system. SQLite is ideal for learning and small-scale applications.

**Code Example: Setting Up a SQLite Database**
```python
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
```

## Inserting Data into the Database

### Inserting Data
Next, let's insert some data into our `users` table.

**Code Example: Inserting Data**
```python
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
```

## Querying Data from the Database

### Querying Data
Now, let's query the data we've inserted into our `users` table.

**Code Example: Querying Data**
```python
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
```

## Updating and Deleting Data

### Updating Data
Let's see how to update existing data in the `users` table.

**Code Example: Updating Data**
```python
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
```

### Deleting Data
Finally, let's delete some data from the `users` table.

**Code Example: Deleting Data**
```python
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
```

## About BotCampus AI

**BotCampus AI** is a leading provider of AI and machine learning education. Our mission is to empower individuals and organizations with the knowledge and skills needed to thrive in the AI-driven world.

### Learning Management System
Access our LMS portal at [learn.botcampus.ai](https://learn.botcampus.ai) for more courses and resources.

### Contact Us
- **Website:** [www.botcampus.ai](https://www.botcampus.ai)
- **Email:** support@botcampus.ai
- **GitHub:** [BotCampus AI on GitHub](https://github.com/Bot-Campus-AI/advanced-python)

Thank you for using this project to enhance your Python journey with BotCampus AI. Enjoy coding!

© 2024 BotCampus AI. All rights reserved.