import sqlite3

# we make a connection
# use the connect method to make one
# args we pass is the name of our db
# if it doesn't exist, it will create one
connection = sqlite3.connect('customers.db')

# NOTE: sqlite allows us to make such a db
# OR make a db in memory, it will disappear once the program closes
# do stuff to it, but it's not permanent

# to do this we type:
# connection = sqlite3.connect(':memory:')

# a cursor will tell the db what I want to do
cursor = connection.cursor()

# create a table
# normally, what python docs recommend is using """ """

# cursor.execute("""
# do stuff
# do some more stuff
# do even more stuff
# """)

cursor.execute("""CREATE TABLE customers (
        first_name text,
        last_name text,
        email text
    )""")

# this works too, but it all has to be a single line string
# cursor.execute("CREATE TABLE customers (first_name DATATYPE, last_name DATATYPE, email DATATYPE)")

# SQLITE has the following data types:
# NULL
# INTEGER
# REAL
# TEXT
# BLOB

# Save (commit) the changes
connection.commit()
# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
connection.close()
