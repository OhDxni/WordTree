import sqlite3

# creating a connection between python and database
conn = sqlite3.connect('users_db.db') #if the file does not exist, it will be created
cursor = conn.cursor()

# cursor.e  EXT NOT NULL"""