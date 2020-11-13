import sqlite3


def show_all():
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute("SELECT * FROM customers")
    data = c.fetchall()
    for item in data:
        print(item)
    conn.commit()
    conn.close()


def add_one(first_name, last_name, email):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute('INSERT INTO customers VALUES (?, ?, ?)', (first_name, last_name, email))
    conn.commit()
    conn.close()


def delete_one(row_id):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    # passing integers to sqlite doesn't work, it has to be strings
    c.execute('DELETE FROM customers WHERE rowid = (?)', str(row_id))
    conn.commit()
    conn.close()


def add_many(list_of_items):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.executemany('INSERT INTO customers VALUES (?, ?, ?)', (list_of_items))
    conn.commit()
    conn.close()


def email_lookup(email):
    conn = sqlite3.connect('customers.db')
    c = conn.cursor()
    c.execute('SELECT * FROM customers WHERE email = (?)', (email,))  # cause it expects a tuple, we add a comma

    data = c.fetchall()
    for item in data:
        print(item)

    conn.commit()
    conn.close()
