import sqlite3

connection = sqlite3.connect("users.db")
cursor = connection.cursor()