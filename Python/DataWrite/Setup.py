import sqlite3
import Statements

### Connecting to database #################
connection = sqlite3.connect("Tog-db.db")
cursor = connection.cursor()
############################################


### Sovevogntype & Sittevogntype
coupeWagon = ("SJ-sovevogn-1", 4)
seatedWagon = ("SJ-sittevogn-1", 4, 3)

try: 
    cursor.execute(Statements.sovevogntype, coupeWagon)
except Exception:
    print("Sovevogn allerede lagt inn.")
try:
    cursor.execute(Statements.sittevogntype, seatedWagon)
except Exception:
    print("Sittevogn allerede lagt inn.")

### Jernbanestasjon
trainStations = [
    ("Bodø", 4.1),
    ("Fauske", 34),
    ("Mo i Rana", 3.5),
    ("Mosjøen", 6.8),
    ("Steinkjer", 3.6),
    ("Trondheim S", 5.1)
]
try:
    cursor.executemany(Statements.jernbanestasjon, trainStations)
except Exception:
    print("Already added stations")

### Operatør
try:
    cursor.execute(Statements.operatør)
except Exception:
    print("Operator already added")

### Delstrekning
# Checking if already added
addedCount = 0
for row in cursor.execute("SELECT delstrekningID FROM Delstrekning"):
    addedCount += 1

if addedCount == 0:
    connections = [
    (None, "enkelt", 60, "Bodø", "Fauske"), #1
    (None, "enkelt", 170, "Fauske", "Mo i Rana"), #2
    (None, "enkelt", 90, "Mo i Rana", "Mosjøen"), #3
    (None, "enkelt", 280, "Mosjøen", "Steinkjer"), #4
    (None, "dobbelt", 120, "Steinkjer", "Trondheim") #5
    ]
    try:
        cursor.executemany(Statements.delstrekning, connections)
    except Exception:
        print("Error on INSERT Delstrekning")
else: 
    print("Delstrekninger allerede lagt inn")

### Banestrekning
addedCount = 0
for row in  cursor.execute("SELECT strekningID FROM Banestrekning"):
    addedCount += 1
if addedCount == 0:
    routes = [
        (None, "dagtog", "diesel", "Trondheim S", "Bodø"), #1
        (None, "nattog", "diesel", "Trondheim S", "Bodø"), #2
        (None, "morgentog", "diesel", "Mo i Rana", "Trondheim S"), #3
    ]
    try:
        cursor.executemany(Statements.banestrekning, routes)
    except Exception:
        print("Error on INSERT Banestrekning")
else:
    print("Banestrekninger allerede lagt inn")


### HarDelstrekning




### Adding changes ###
connection.commit()
connection.close()
######################