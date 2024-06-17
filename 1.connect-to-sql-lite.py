from sqlalchemy import create_engine

# Creating an engine
engine = create_engine('sqlite:///example.db')

# Connecting to the database
connection = engine.connect()
print("Connected to the database successfully.")
