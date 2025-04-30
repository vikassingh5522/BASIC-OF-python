# Creating table using Python:

import sqlite3

con = sqlite3.connect("test.db")

cur = con.cursor()
# Cursor() is a class which having methods like execute(), fetchall(), fetchmany(), fetchone(), etc. and if we want to access cursor class methods therefore we need to create object of cursor class and then only we can call methods under cursor() class

cur is the object of cursor() class

# It is an object that is used to make the connection for executing SQL queries. 

# It acts as middleware between SQLite database connection and SQL query. It is created after giving connection to SQLite database.

# So whenever we want SQL operations like create table, insert, select, etc. we need to open cursor() first and then only we can execute SQL queries.

Syntax: cursor_object = connection_object.cursor()

cursor_object.execute("CREATE TABLE <table_name> (column_name INTEGER PRIMARYKEY AUTOINCREAMENT, second_column_name TEXT, third_column_name TEXT, Fourth_column_name INTEGER)")

cur.execute("create table students(s_id integer primarykey autoincreament,name text,last_name text,contact integer)")

# Only to first column that is to id, we need to give primarykey as well autoincreament to other column name just give column name and datatype.

# SQLite is a case insensitive. Table names and column names can be typed in uppercase, lowercase, or mixed case, and different capitalizations of the same database object name can be used interchangeably.

print("Table created successfully...")

con.close()
# It is good stadard to close database connection which we build using con connection_object


Insert Data into SQLite Table using Python:

# For again SQL Operations we need to import sqlite3 module and then build connection and then using cursor insert query execute.

import sqlite3

con = sqlite3.connect("test.db")

cur = con.cursor()

# Insert Query Syntax: insert into <table_name>(column_names) values ("data")
cur.execute("insert into students(name,last_name,contact) values ('ramesh','patil',1234567890)")

# Data should be in single quote only for text column names and for integer column single quotes are optional 

# Note: In Insert Query NO need to give id column name as it is primarykey and autoincreatement so automatically it will increament in integer format.

#  In cur.execute() when we use multiple lines by pressing enter, to avoid syntax error, we can use three quotes before query starts and three quotes end of the query use.

#  in cur.execute(""" insert into
#  table_name(name, last_name, contact)
#  values('ramesh','patil','1234567890')""")

print("Data Inserted Successfully..")

con.commit()
# using commit() data will be saved in table which we mention above,
# compulsory we need to write connection_object.commit() for saving data.

con.close()












