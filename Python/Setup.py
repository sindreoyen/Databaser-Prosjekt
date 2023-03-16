import sqlite3

# Connecting to database
connection = sqlite3.connect("./Tog-db.db")
# Setting up DB cursor
cursor = connection.cursor()

# Wagon types
coupeWagon = ("SJ-sovevogn-1", 4)
seatedWagon = ("SJ-sittevogn-1", 4, 3)

cursor.execute("INSERT INTO Sovevogntype VALUES(?, ?)", coupeWagon)
cursor.execute("INSERT INTO Sittevogntype VALUES(?,?,?)", seatedWagon)

# Train stations
trainStations = [
    ("Bodø", 4.1),
    ("Fauske", 34),
    ("Mo i Rana", 3.5),
    ("Mosjøen", 6.8),
    ("Steinkjer", 3.6),
    ("Trondheim S", 5.1)
]
try:
    cursor.executemany("INSERT INTO Jernbanestasjon VALUES(?, ?)", trainStations)
except Exception:
    print("Already added stations")

# Operator
try:
    cursor.execute("INSERT INTO Operatør VALUES('SJ')")
except Exception:
    print("Operator already added")

# Train-rides


# Adding changes
connection.commit()
connection.close()