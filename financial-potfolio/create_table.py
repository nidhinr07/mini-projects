# import sqlite3
#
# connection = sqlite3.connect("users.db")
# cursor = connection.cursor()

from database import connection, cursor

# ================= USER TABLE =================

cursor.execute('''
CREATE TABLE users
(
    user_name TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL,
    balance REAL NOT NULL
)
''')


# ================= INVESTMENT TABLE =================

cursor.execute('''
CREATE TABLE investment
(
    investment_id INTEGER PRIMARY KEY,
    company_name TEXT NOT NULL UNIQUE,
    type TEXT NOT NULL,
    price REAL NOT NULL,
    quantity INTEGER NOT NULL
)
''')


# ================= PORTFOLIO TABLE =================

cursor.execute('''
CREATE TABLE portfolio
(
    user_name TEXT NOT NULL,
    investment_id INTEGER NOT NULL,
    quantity INTEGER NOT NULL,
    purchase_price REAL NOT NULL,

    PRIMARY KEY (user_name, investment_id),

    FOREIGN KEY (user_name) REFERENCES users(user_name),
    FOREIGN KEY (investment_id) REFERENCES investment(investment_id)
)
''')


# ================= TRANSACTIONS TABLE =================

cursor.execute('''
CREATE TABLE transactions
(
    transaction_id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_name TEXT NOT NULL,
    investment_id INTEGER NOT NULL,
    transaction_type TEXT NOT NULL,
    quantity INTEGER NOT NULL,
    price REAL NOT NULL,
    total_amount REAL NOT NULL,
    transaction_date DATETIME DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (user_name) REFERENCES users(user_name),
    FOREIGN KEY (investment_id) REFERENCES investment(investment_id)
)
''')


connection.commit()
connection.close()