import sqlite3

conn = sqlite3.connect('customers.db')
c = conn.cursor()

# c.execute("""INSERT INTO customers  values ('John', 'John', 'some@mail.com')""")
# c.execute("""INSERT INTO customers  values ('Hulk', 'Smash', 'some_other@mail.com')""")
# provide the tuple to insert
c.execute("""INSERT INTO customers  values ('Mary', 'Sue', 'mary@sue.com')""")
print('command executed successfully')


conn.commit()
conn.close()
