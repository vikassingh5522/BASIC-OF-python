# Python SQLite Database:

# Python SQLite3 Module:

# Python SQLite3 module is used to integrate the SQLite database with Python.

# Using SQLite3 Module you can perform all possible DB operations like creating database, creating table and performing various operations on table.

# SQLite3 Module implements the python DB API Interface to be a compliant (standard) solution for implementing SQL ( Structured Query Language ) related operations in program.

# SQLite is probably the most straight forward database to connect to with a Python application since you don't need to install any external Python SQL modules to do so. By default, your Python installation contains a Python SQL library named sqlite3 that you can use to interact with an SQLite database

# Connecting SQLite Database through Python:

# As mention using SQLite3 module we can integrate SQLite Database therefore as we import any module similarly we can import sqlite3 module in our program and can connect sqlite database through python.

import sqlite3
# compulsory we need to import sqlite3 module for performing databse related operations.

con = sqlite3.connect("test.db")
# con is connection_object for database
# test is the database name, if already exist with this name database then it opens db and operations will perform in same db else new DB will create.

print("Database is created or Opened Successfully!")

# as soon as you run .py file, you can see print() message will dispay and test.db is created in your folder.










