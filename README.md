# Connecting to Databases with SQLAlchemy

## Overview
This tutorial explores how to connect to databases using SQLAlchemy, a powerful SQL toolkit and Object-Relational Mapping (ORM) library for Python. The script guides learners through setting up SQLAlchemy, connecting to a database, and performing basic operations such as creating tables, inserting data, querying data, updating data, and deleting data.

## Table of Contents
1. [Practical Applications of SQLAlchemy](#practical-applications-of-sqlalchemy)
2. [Introduction to SQLAlchemy](#introduction-to-sqlalchemy)
3. [Setting Up SQLAlchemy](#setting-up-sqlalchemy)
4. [Connecting to a Database](#connecting-to-a-database)
5. [Creating Tables](#creating-tables)
6. [Inserting Data](#inserting-data)
7. [Querying Data](#querying-data)
8. [Updating and Deleting Data](#updating-and-deleting-data)
9. [About BotCampus AI](#about-botcampus-ai)

## Practical Applications of SQLAlchemy

### Practical Applications
SQLAlchemy simplifies database interactions and provides an efficient way to manage database operations in Python. It is essential for building data-driven applications, data analytics pipelines, and complex data-driven systems.

**Examples:**
- Web development with Flask
- Data analytics
- Enterprise applications

## Introduction to SQLAlchemy

### What is SQLAlchemy?
SQLAlchemy is a SQL toolkit and ORM library for Python. It provides a full suite of enterprise-level persistence patterns designed for efficient and high-performing database access.

**Visuals:**
- Overview of SQLAlchemy's two main components: the Core (for direct SQL access) and the ORM (for object-relational mapping).

## Setting Up SQLAlchemy

### Setting Up SQLAlchemy
To start, you need to install SQLAlchemy using pip.

**Installation:**
```bash
pip install sqlalchemy
```

**Visuals:**
- Show the installation process in the terminal.

## Connecting to a Database

### Connecting to a Database
Connect to a SQLite database using SQLAlchemy by importing the necessary modules and creating an engine.

**Code Example: Connecting to a SQLite Database**
```python
from sqlalchemy import create_engine

# Creating an engine
engine = create_engine('sqlite:///example.db')

# Connecting to the database
connection = engine.connect()
print("Connected to the database successfully.")
```

**Visuals:**
- Show the code being written and executed, displaying the output.
- Highlight the process of creating an engine and connecting to the database.

## Creating Tables

### Creating Tables
Define your database schema using Python classes and create a `User` table.

**Code Example: Creating Tables**
```python
from sqlalchemy import Column, Integer, String, MetaData, Table

# Creating a metadata object
metadata = MetaData()

# Defining the User table
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('age', Integer),
    Column('email', String)
)

# Creating the table in the database
metadata.create_all(engine)
print("Table created successfully.")
```

**Visuals:**
- Show the code being written and executed, displaying the output.
- Highlight the process of defining and creating tables using SQLAlchemy.

## Inserting Data

### Inserting Data
Insert data into the `users` table.

**Code Example: Inserting Data**
```python
from sqlalchemy import insert

# Creating an insert statement
stmt = insert(users).values(name='Raj Kumar', age=30, email='raj.kumar@example.com')
connection.execute(stmt)

stmt = insert(users).values(name='Amit Sharma', age=25, email='amit.sharma@example.com')
connection.execute(stmt)

print("Data inserted successfully.")
```

**Visuals:**
- Show the code being written and executed, displaying the output.
- Highlight the process of inserting data using SQLAlchemy.

## Querying Data

### Querying Data
Query the data inserted into the `users` table.

**Code Example: Querying Data**
```python
from sqlalchemy import select

# Creating a select statement
stmt = select([users])
result = connection.execute(stmt)

# Printing the queried data
for row in result:
    print(row)

print("Data queried successfully.")
```

**Visuals:**
- Show the code being written and executed, displaying the output.
- Highlight the process of querying data using SQLAlchemy.

## Updating and Deleting Data

### Updating Data
Update existing data in the `users` table.

**Code Example: Updating Data**
```python
from sqlalchemy import update

# Creating an update statement
stmt = update(users).where(users.c.name == 'Raj Kumar').values(age=31)
connection.execute(stmt)

print("Data updated successfully.")
```

**Visuals:**
- Show the code being written and executed, displaying the output.
- Highlight the process of updating data using SQLAlchemy.

### Deleting Data
Delete data from the `users` table.

**Code Example: Deleting Data**
```python
from sqlalchemy import delete

# Creating a delete statement
stmt = delete(users).where(users.c.name == 'Amit Sharma')
connection.execute(stmt)

print("Data deleted successfully.")
```

**Visuals:**
- Show the code being written and executed, displaying the output.
- Highlight the process of deleting data using SQLAlchemy.

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