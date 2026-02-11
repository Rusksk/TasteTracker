
import sqlite3
conn = sqlite3.connect("tastetracker.db")
c = conn.cursor()
c.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
c.execute("CREATE TABLE IF NOT EXISTS reviews (id INTEGER PRIMARY KEY, restaurant TEXT, rating INTEGER, user_id INTEGER)")
conn.commit()
conn.close()
