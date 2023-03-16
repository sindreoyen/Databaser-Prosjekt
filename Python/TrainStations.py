import sqlite3

# Connecting to database
connection = sqlite3.connect("./Tog-db.db")
# Setting up DB cursor
cursor = connection.cursor()

# Train stations
trainStations = [
    ("Bodø", 4.1),
    ("Fauske", 34),
    ("Mo i Rana", 3.5),
    ("Mosjøen", 6.8),
    ("Steinkjer", 3.6),
    ("Trondheim", 5.1)
]
cursor.executemany("INSERT INTO Jernbanestasjon VALUES(?, ?)", trainStations)
connection.commit()
connection.close()