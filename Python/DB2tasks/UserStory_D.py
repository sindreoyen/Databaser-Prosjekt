import sqlite3
import datetime
import LocalData

### Connecting to database #################
connection = LocalData.getDBConnection()
cursor = connection.cursor()
############################################

### Get station mapping
stationList = []
for row in cursor.execute("""SELECT Delstrekning.stasjon1, Delstrekning.stasjon2
FROM Delstrekning
NATURAL JOIN HarDelstrekning
NATURAL JOIN Banestrekning
WHERE Banestrekning.navn = 'Nordlandsbanen'"""):
    stationList.append(row)

stationDict = {}
for tuple in stationList: 
    try:
        stationDict[tuple[0]].append(tuple[1])
    except Exception:
        stationDict[tuple[0]] = [tuple[1]]
    try:
        stationDict[tuple[1]].append(tuple[0])
    except Exception:
        stationDict[tuple[1]] = [tuple[0]]
#####################################################


### Get user input for stations - find directions ###
startStation = ""
endStation = ""
print("\n\n# VELG STASJONER #")
print("- Stasjoner: ", str(stationDict.keys()).removeprefix("dict_keys(").removesuffix(")"), " -")

while startStation == "":
    stationInput = input("Velg startstasjon: ")
    try:
        stationDict[stationInput]
        startStation = stationInput
    except Exception:
        print("OBS! Stasjonen eksisterer ikke. Velg på nytt.")

while endStation == "" or startStation == endStation:
    stationInput = input("Velg endestasjon: ")
    try:
        stationDict[stationInput]
        endStation = stationInput
    except Exception:
        print("OBS! Stasjonen eksisterer ikke. Velg på nytt.")

withMainDir: int = -1 #1 if you're moving with the main direction, 0 otherwise
if endStation == "Trondheim S" or startStation == "Bodø":
    withMainDir = 0
elif endStation == "Bodø" or startStation == "Trondheim S":
    withMainDir = 1

def findIndex() -> int:
    attemptIndex = 0
    
    prevStation: str = startStation
    while prevStation != endStation:
        # Checking whether the direction faces Trondheim S
        try:
            nextStation = stationDict[prevStation][attemptIndex]
            prevStation = nextStation
        except Exception:
            print("Error checking stations")
        if nextStation == endStation:
            return attemptIndex
        if nextStation == "Trondheim S":
            return 1

if withMainDir == -1:
    withMainDir = findIndex()

####################################################
### Find all Togrute with this direction
togruteIDs: list = list() ## all available togruter
for row in cursor.execute("SELECT ruteID from Togrute WHERE medHovedRetning = ?", (withMainDir,)):
    togruteIDs.append(row[0])

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
    LEFT OUTER NATURAL JOIN 
    KjørerStrekning KS
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