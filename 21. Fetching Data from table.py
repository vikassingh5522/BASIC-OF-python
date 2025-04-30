Fetching Data from SQLite Table using Python:

import sqlite3

con = sqlite3.connect("test.db")

cur = con.cursor()

# Select Query Syntax: select * from <table_name>
cur.execute("select rowid, * from students")

# write rowid, to show primary key sr. no. on screen
# con.commit()
# as for inserting data we use connection_object.commit() function to save data into table, now for fetching data from table.

# Using cursor object we can access three methods as :
# fetchall()
# fetchmany()
# fetchone()
# rowcount

# we can call these methods for accessing data from table by using cursor object

cur.fetchall()

# to show data on screen we need to call this in print()

print(cur.fetchall())

# to display data in row-wise format then use:

data = cur.fetchall()
for x in data:
  print(x)


con.close()