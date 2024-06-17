from sqlalchemy import create_engine, Column, Integer, String, MetaData, Table, insert

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

# Creating an insert statement
stmt = insert(users).values(name='Raj Kumar', age=30, email='raj.kumar@example.com')
connection.execute(stmt)

stmt = insert(users).values(name='Amit Sharma', age=25, email='amit.sharma@example.com')
connection.execute(stmt)

print("Data inserted successfully.")
