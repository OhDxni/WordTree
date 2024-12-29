import sqlite3

from Project_Code.game_logic import project_root

# creating a connection between python and database
# conn = sqlite3.connect('../databases/users_db.db')  #if the file does not exist, it will be created
conn = sqlite3.connect(f"{project_root}/databases/users_db.db")

cursor = conn.cursor()


# creating a table that will store usernames and hashed passwords
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    password TEXT NOT NULL,
    best_4 INT,
    second_4 INT,
    third_4 INT,
    best_5 INT,
    second_5 INT,
    third_5 INT,
    best_6 INT,
    second_6 INT,
    third_6 INT
    )""")

conn.close()