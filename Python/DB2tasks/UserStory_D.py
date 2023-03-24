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
    timestamp_str = "2023-04-03 07:00" # input("Vennligst skriv inn tid på formatet: 'YYYY-MM-DD hh:mm': ")
    try:
        date = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M")
        valid = True
    except ValueError:
        print("Formatet ble ikke korrekt. Vennligst prøv igjen.")

# Valid timestamp
######################################################################################
### OBS! Antar ut fra oppgavens ordlyd at *alle* tog samme og neste dag skal vises ###
######################################################################################
minDate = (date - datetime.timedelta(hours=date.time().hour, minutes=date.time().minute))
minTime = minDate.timestamp()
maxTime = (minDate + datetime.timedelta(days=1)).timestamp()

### Find Togruteforekomst
forekomster = [] #contains the id's of all Togrute with a Forekomst on the given day
hadResult = False

trains: list = []
for id in togruteIDs:
    statement = """
    SELECT DATE(Tf.dato, 'unixepoch', 'localtime'), 
    KS.tidStasjon1, 
    KS.tidStasjon2, 
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
        train: tuple = (str(row[0]), 
                        Utilities.getTimeString(unixTime=row[1 if withMainDir else 2]), 
                        str(row[5]))
        trains.append(train)
        hadResult = True

if not hadResult:
    print("Beklager, ingen tilgjengelige tog.")
else:
    ## Had an error with sqlite3 where the ORDER BY did not work
    ## made a manual sorting below
    def sortKey(e: tuple):
        return e[0]
    trains.sort()
    for train in trains:
        print(train[0] + ": Toget,", train[2], "går fra", startStation, "kl:", train[1])

### Adding changes ###
connection.close()
######################