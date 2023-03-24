import sqlite3
import datetime

### Utilities - find stations
def findStationsDirection(connection: sqlite3.Connection) -> tuple:
    """Returns: startStation, endStation, withMainDir"""
    ### Get station mapping
    cursor = connection.cursor()
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
    return startStation, endStation, withMainDir

### Utilities - find Togrute with direction
def getTogruteWithDir(connection: sqlite3.Connection,
                      dir: int) -> list:
    cursor = connection.cursor()
    togruteIDs = []
    for row in cursor.execute("SELECT ruteID from Togrute WHERE medHovedRetning = ?", (dir,)):
        togruteIDs.append(row[0])
    return togruteIDs

def getTimeString(unixTime: int) -> str:
    return datetime.datetime.utcfromtimestamp(unixTime).time()