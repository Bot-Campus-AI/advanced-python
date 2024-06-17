from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table

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
print("Table created successfully.")
