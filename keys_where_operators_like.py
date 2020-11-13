import sqlite3

conn = sqlite3.connect('customers.db')
c = conn.cursor()

# query the db
# rowid will gets us the primary key, since we didn't make any, we get the generic ones
# from 1 to len(number of entries)
# returns (2, 'Hulk', 'Smash', 'some_other@mail.com')

# c.execute("SELECT rowid, * FROM customers")
# --------------------------------------------------------

# WHERE clause, specify the query
# return entries which have a last name "Smash"
# some other operators
# =, >, <, >=, <=
# c.execute('SELECT * FROM customers WHERE last_name = "Smash"')
# --------------------------------------------------------

# the LIKE operator is used in a WHERE clause to search for a specified pattern in a column
# There are two wildcards often used in conjunction with the LIKE operator:
#
# % - The percent sign represents zero, one, or multiple characters
# _ - The underscore represents a single character

# c.execute('SELECT * FROM customers WHERE last_name LIKE "Sm%" OR first_name LIKE "St%"')
# returns
# ('Hulk', 'Smash', 'some_other@mail.com')
# ('Steph', 'Curry', 'steph@curry.com')
# --------------------------------------------------------

# looks for a pattern: <anything, any characters> + '@' + <anything, any characters>
# c.execute('SELECT * FROM customers WHERE email LIKE "%@%"')
# --------------------------------------------------------

# of course, can be written like this too
c.execute("""
    SELECT *
    FROM customers
    WHERE email LIKE "%@%"
""")

data = c.fetchall()
for entry in data:
    print(entry)

conn.commit()
conn.close()
