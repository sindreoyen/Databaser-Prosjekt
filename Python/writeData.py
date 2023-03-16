import sqlite3

# Connecting to database
connection = sqlite3.connect("./Tog-db.db")
# Setting up DB cursor
cursor = connection.cursor()

# cursor.execute(" ... ")