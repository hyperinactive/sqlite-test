import sqlite3

conn = sqlite3.connect('customers.db')
c = conn.cursor()

many_customers = [
    ('Wes', 'Brown', 'wes@brown.com'),
    ('Peter', 'Parker', 'peter@paker.com'),
    ('Steph', 'Curry', 'steph@curry.com')
]

# execute many does exactly what is says
# ? is a placeholder for any values we've inserting into the database
c.executemany("INSERT INTO customers VALUES (?,?,?)", many_customers)

print('command executed successfully')
conn.commit()
conn.close()
