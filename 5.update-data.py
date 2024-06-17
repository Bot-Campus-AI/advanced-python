from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table
from sqlalchemy import update
# Creating an engine
engine = create_engine('sqlite:///example.db')

# Connecting to the database
connection = engine.connect()
print("Connected to the database successfully.")

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

# Inserting some data into the table (for demonstration purposes)
connection.execute(users.insert(), [
    {'name': 'Raj', 'age': 25, 'email': 'raj@example.com'},
    {'name': 'Amit', 'age': 30, 'email': 'amit@example.com'},
    {'name': 'Priya', 'age': 22, 'email': 'priya@example.com'},
    {'name': 'Sara', 'age': 27, 'email': 'sara@example.com'}
])

# Creating an update statement
stmt = update(users).where(users.c.name == 'Raj Kumar').values(age=31)
connection.execute(stmt)

print("Data updated successfully.")
