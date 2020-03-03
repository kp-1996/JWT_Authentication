import sqlite3
from flask import jsonify

class Database:
    def __init__(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()
        query = "CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, username text, password text)"
        cursor.execute(query)

        connection.commit()
        connection.close()
