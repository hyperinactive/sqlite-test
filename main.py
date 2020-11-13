import database

# add a record
# database.add_one('Ash', 'Ketchum', 'ash@ketchum.com')
# --------------------------------------------------------

# add multiple items
# many_customers = [
#     ('Electro', 'Lyte', 'electro@lyte.com'),
#     ('Petah', 'Parkah', 'petah@parkah.com'),
#     ('Anthony', 'Davis', 'anthony@davis.com')
# ]

# database.add_many(many_customers)
# --------------------------------------------------------

# delete an item
# database.delete_one(7)
# --------------------------------------------------------

# lookup something
database.email_lookup('steph@curry.com')
# --------------------------------------------------------

# show all records
# database.show_all()
