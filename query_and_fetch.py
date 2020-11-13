import sqlite3

conn = sqlite3.connect('customers.db')
c = conn.cursor()

# query the db
c.execute("SELECT * FROM customers")

# 3 options
# c.fetchone()
# c.fetchmany(self,size)
# c.fetchall()

# prints all the table entries
# returns a list of tuples
# print(c.fetchall())

# prints just the first entry
# returns a tuple
# print(c.fetchone())

# prints n entries
# print(c.fetchmany(3))

data = c.fetchall()
print(data)

print('NAME \t\t| EMAIL ')
print('------------------------')

for entry in data:
    print(f'{entry[0]} {entry[1]} | \t {entry[2]}')

conn.commit()
conn.close()
