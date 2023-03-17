import sqlite3
import Statements

### Connecting to database #################
connection = sqlite3.connect("./Tog-db.db")
cursor = connection.cursor()
############################################


### Wagon types
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

### Train stations
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

### Operator
try:
    cursor.execute(Statements.operatør)
except Exception:
    print("Operator already added")

### Delstrekninger
# Checking if already added
addedCount = 0
for row in cursor.execute("SELECT delstrekningID FROM Delstrekning"):
    addedCount += 1

if addedCount == 0:
    connections = [
    (None, "enkelt", 60, "Bodø", "Fauske"),
    (None, "enkelt", 170, "Fauske", "Mo i Rana"),
    (None, "enkelt", 90, "Mo i Rana", "Mosjøen"),
    (None, "enkelt", 280, "Mosjøen", "Steinkjer"),
    (None, "dobbelt", 120, "Steinkjer", "Trondheim")
    ]
    try:
        cursor.executemany(Statements.delstrekning, connections)
    except Exception:
        print("Error on INSERT Delstrekning")
else: 
    print("Delstrekninger allerede lagt inn")

### Banestrekninger
addedCount = 0
for row in  cursor.execute("SELECT strekningID FROM Banestrekning"):
    addedCount += 1
if addedCount == 0:
    routes = [
        (None, "dagtog", "diesel", "Trondheim S", "Bodø"),
        (None, "nattog", "diesel", "Trondheim S", "Bodø"),
        (None, "morgentog", "diesel", "Mo i Rana", "Trondheim S"),
    ]
    try:
        cursor.executemany(Statements.banestrekning, routes)
    except Exception:
        print("Error on INSERT Banestrekning")
else:
    print("Banestrekninger allerede lagt inn")

# Connecting to Delstrekning
for row in cursor.execute("SELECT strekningID, startstasjonNavn, sluttstasjonNavn FROM Banestrekning"):
    id = row[0]
    start, end = row[1], row[2]
    # Connect delstrekning



### Adding changes ###
connection.commit()
connection.close()
######################