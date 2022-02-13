import sqlite3
from config import DB_FILE

conn = sqlite3.connect(DB_FILE, detect_types=sqlite3.PARSE_DECLTYPES)
cursor = conn.cursor()

# Creating DB
cursor.execute('CREATE TABLE DATA(id INTEGER PRIMARY KEY, name TEXT, surname TEXT, mail TEXT, sign array)')

conn.commit()

cursor.close()
conn.close()