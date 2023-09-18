import sqlite3
from faker import Faker
import random

with sqlite3.connect('hillel.db') as con:
    cur = con.cursor()
    cur.execute("""DROP TABLE IF EXISTS customers""")
    cur.execute("""CREATE TABLE IF NOT EXISTS customers (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL
        )""")
    cur.execute("""DROP TABLE IF EXISTS tracks""")
    cur.execute("""CREATE TABLE IF NOT EXISTS tracks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        duration INTEGER NOT NULL
        )""")

fake = Faker(['it_IT', 'en_US'])

for i in range(10):
    first_name = fake.first_name()
    last_name = fake.last_name()
    cur.execute(
        """INSERT INTO customers (first_name, last_name) VALUES (?, ?)""",
        (first_name, last_name)
    )

for i in range(10):
    name = fake.text()
    duration = random.randint(100, 300)
    cur.execute(
        """INSERT INTO tracks (name, duration) VALUES (?, ?)""",
        (name, duration)
    )
con.commit()
con.close()
