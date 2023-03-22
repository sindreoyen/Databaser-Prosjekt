import sqlite3
import datetime
import LocalData
import Utilities

### Connecting to database #################
connection = LocalData.getDBConnection()
cursor = connection.cursor()
############################################

res = Utilities.findStationsDirection(connection=connection)
startStation: str = res[0]
endStation: str = res[1]
withMainDir: int = res[2]

### Find all Togrute with this direction
togruteIDs: list = Utilities.getTogruteWithDir(
    connection=connection, dir=withMainDir)

### Select date and time
valid = False
date: datetime
while not valid:
    timestamp_str = input("Vennligst skriv inn tid på formatet: 'YYYY-MM-DD hh:mm': ")
    try:
        date = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M")
        valid = True
    except ValueError:
        print("Formatet ble ikke korrekt. Vennligst prøv igjen.")

# Valid timestamp
minDate = (date - datetime.timedelta(hours=date.time().hour, minutes=date.time().minute))
minTime = minDate.timestamp()
maxTime = (minDate + datetime.timedelta(days=1)).timestamp()

### Find Togruteforekomst
forekomster = [] #contains the id's of all Togrute with a Forekomst on the given day
hadResult = False
for id in togruteIDs:
    statement = """
    SELECT DATE(Tf.dato, 'unixepoch', 'localtime'), 
    TIME(KS.tidStasjon1, 'unixepoch', 'localtime'), 
    TIME(KS.tidStasjon2, 'unixepoch', 'localtime'), 
    Ds.stasjon1, Ds.stasjon2, Tf.navn
    FROM 
    Togruteforekomst Tf 
    LEFT OUTER NATURAL JOIN KjørerStrekning KS
    LEFT OUTER NATURAL JOIN Delstrekning Ds
    WHERE Tf.ruteID=?"""
    postfix = ("1" if withMainDir == 1 else "2")
    statement += " AND Ds.stasjon" + postfix + "='" + startStation + "'"
    statement += " AND Tf.dato>=" + str(minTime) + " AND Tf.dato <=" + str(maxTime)
    statement += "\nORDER BY Tf.dato, KS.tidStasjon" + postfix + " DESC"
    for row in cursor.execute(statement, (id,)):
        date = row[0]
        startTime = row[1 if withMainDir else 2]
        name = row[5]
        print(date + ": Toget,", name, "går fra", startStation, "kl:", startTime)
        hadResult = True

if not hadResult:
    print("Beklager, ingen tilgjengelige tog.")

### Adding changes ###
connection.close()
######################