import sqlite3
import bcrypt

DATABASE = "database/passwords.db"

def create_table():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("""
                CREATE TABLE IF NOT EXISTS passwords(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                password_hash TEXT
                )
               """)
    conn.commit()
    conn.close()

def password_exists(password):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()
    cur.execute("SELECT password_hash FROM passwords")
    rows = cur.fetchall()
    conn.close()

    for row in rows:
        if bcrypt.checkpw(password.encode(), row[0].encode()):
            return True
    return False

def save_password(password):
    conn =  sqlite3.connect(DATABASE)
    cur = conn.cursor()

    hashed = bcrypt.hashpw(
        password.encode(),
        bcrypt.gensalt()
    ).decode()

    cur.execute(
        "INSERT INTO passwords(password_hash) VALUES(?)",
        (hashed,)
    )

    conn.commit()
    conn.close()
    