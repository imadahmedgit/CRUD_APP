import os
import sqlite3

# Removes pre existing db
# if os.path.exists('crud.db'):
#     os.remove('crud.db')

#Create Database

conn = sqlite3.connect('crud.db')
c = conn.cursor()

# Users Table
c.execute("""CREATE TABLE IF NOT EXISTS "users" (
    "user_id"    INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    "first_name" TEXT,
    "last_name"  TEXT,
    "email"      TEXT,
    "date_created" TEXT,
    "active"     TEXT
)""")

# Orders Table
c.execute("""CREATE TABLE IF NOT EXISTS orders (
    order_id   INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    order_date TEXT,
    status     TEXT,
    user_id    INTEGER,
    FOREIGN KEY (user_id)
    REFERENCES users (user_id) 
)""")

# Scenes Table
c.execute("""CREATE TABLE IF NOT EXISTS scenes (
    scene_id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name      TEXT,
    s_status  TEXT,
    sensor    TEXT,
    order_id  INTEGER,
    FOREIGN KEY (order_id)
    REFERENCES orders (order_id) 
)""")


conn.row_factory = sqlite3.Row

# Helper methods for running SQL queries
def sql_query(query):
    cur = conn.cursor()
    cur.execute(query)
    rows = cur.fetchall()
    return rows

def sql_edit_insert(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    conn.commit()

def sql_delete(query,var):
    cur = conn.cursor()
    cur.execute(query,var)

def sql_query2(query,var):
    cur = conn.cursor()
    cur.execute(query,var)
    rows = cur.fetchall()
    return rows