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

### Partial rides
connections = [
    ("enkel", 60, "Bodø", "Fauske"),
    ("enkel", 170, "Fauske", "Mo i Rana"),
    ("enkel", 90, "Mo i Rana", "Mosjøen"),
    ("enkel", 280, "Mosjøen", "Steinkjer"),
    ("dobbel", 120, "Steinkjer", "Trondheim")
]
#try:
cursor.executemany(Statements.delstrekning, connections)
#except Exception:
 #   print("Error inserting into Delstrekning")


### Adding changes ###
connection.commit()
connection.close()
######################