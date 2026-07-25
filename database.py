import sqlite3

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    email TEXT UNIQUE,
    password TEXT,
    age INTEGER,
    gender TEXT,
    college TEXT,
    degree TEXT,
    branch TEXT,
    year TEXT,
    cgpa TEXT,
    company TEXT,
    skills TEXT,
    interests TEXT,
    workmode TEXT,
    goal TEXT
)
""")

conn.commit()
conn.close()

print("Database Created Successfully!")