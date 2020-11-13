import sqlite3

conn = sqlite3.connect('customers.db')
c = conn.cursor()

# UPDATE <name of the table>
# use the SET operator, indicate what gets updated
# in this example, first item in the db gets updated
# c.execute("""
#     UPDATE customers SET first_name = 'Bob'
#     WHERE rowid = 1
# """)
#
# conn.commit()
# --------------------------------------------------------

# DELETE and item
# c.execute("DELETE FROM customers WHERE rowid = 6")
# --------------------------------------------------------

# DROP THE TABLE
# c.execute("DROP TABLE customers")
# ORDER BY orders a list of items
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid")
# DESC -> descending order
# c.execute("SELECT rowid, * FROM customers ORDER BY rowid DESC")

# LIMIT
# AND OR
c.execute("SELECT rowid, * FROM customers ORDER BY first_name LIMIT 2")

data = c.fetchall()
for entry in data:
    print(entry)

conn.commit()
conn.close()
