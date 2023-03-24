import LocalData
import Validators
import datetime
import time

### Connecting to database #################
connection = LocalData.getDBConnection()
cursor = connection.cursor()
############################################


##Validate if epost exist in db
user: tuple = None
while user == None:
    email = input("Hei! Vennligst skriv eposten til brukeren du ønsker å sjekke reiser for: ")
    user = Validators.fetchUser(email=email, connection=connection)
    print("Her er dine fremtidige reiser:")

## Get out data from db about seat orders
cursor.execute("""SELECT Kundeordre.ordreNR, SetebillettIOrdre.seteNR, vognNR, Togrute.ruteID, TogruteForekomst.dato, MAX(Delstrekning.delstrekningID) , MIN(Delstrekning.delstrekningID), Togrute.medHovedRetning
FROM Kundeordre
NATURAL Join Kunde
INNER JOIN TogruteForekomst USING (ruteID, dato)
NATURAL JOIN Togrute
NATURAL JOIN BillettIOrdre
NATURAL JOIN SetebillettIOrdre
NATURAL JOIN Delstrekning
NATURAL JOIN VognIOppsett
NATURAL JOIN KjørerStrekning
WHERE Kunde.epost = ?
GROUP BY ordreNR,vognNR, seteNR""", (email,))
times = cursor.fetchall()

# Get out data from db about cabin orders 
cursor.execute("""SELECT Kundeordre.ordreNR, Togrute.ruteID, TogruteForekomst.dato, Togrute.medHovedRetning, kupeNR, sengNR, reiserFra, reiserTil, vognNR
FROM Kundeordre
NATURAL Join Kunde
INNER JOIN TogruteForekomst USING (ruteID, dato)
NATURAL JOIN Togrute
NATURAL JOIN BillettIOrdre
NATURAL JOIN HarKupeBillett
NATURAL JOIN VognIOppsett
NATURAL JOIN KjørerStrekning
WHERE Kunde.epost = ? 
GROUP BY ordreNR, vognNR, kupeNR, sengNR""", (email,))

kupéBillettInfo = cursor.fetchall()

#time
timeNow = int (time.time())

# Function for finding delstrekningID from a stationName
def findDelstrekningID(stationName, medHovedretning, ruteID):
    query = """SELECT delstrekningID
    FROM Delstrekning
    NATURAL JOIN KjørerStrekning """
    if medHovedretning:
        query += "WHERE Delstrekning.stasjon1 = ? AND ruteID = ?"
    else:
        query += "WHERE Delstrekning.stasjon2 = ? AND ruteID = ?"
    cursor.execute(query, (stationName, ruteID,))
    return cursor.fetchall()[0][0]


# Functions for finding station
def findMinStation(stationID):
    cursor.execute("""SELECT Delstrekning.stasjon1 
    FROM Delstrekning
    WHERE delstrekningID = ?""",(stationID,))
    station = cursor.fetchall()
    return station[0][0]

def findMaxStation(stationID):
    cursor.execute("""SELECT Delstrekning.stasjon2 
    FROM Delstrekning
    WHERE delstrekningID = ?""",(stationID,))
    station = cursor.fetchall()
    return station[0][0]

# Function for finding arrivaltime on a selected station
def findTime(rute_id: int, dato: str, delstrekning_id: int, med_hovedretning: bool, type_stasjon: int) -> int:
    """Find time based on rute ID, date, station ID, direction and station type."""
    query = "SELECT KjørerStrekning.tidStasjon1, KjørerStrekning.tidStasjon2 "
    query += "FROM TogruteForekomst NATURAL JOIN KjørerStrekning "
    query += "WHERE ruteID = ? AND dato = ? AND delstrekningID = ?"
    cursor.execute(query, (rute_id, dato, delstrekning_id,))
    result = cursor.fetchall()[0]

    if med_hovedretning:
        return result[type_stasjon]
    else:
        return result[1 - type_stasjon]

## Make dict with all orders
orderDict = {}
## Add information about seat tickets to orders
for row in times:
    if row[0] not in orderDict.keys():
        order = []
        wagonNR = []
        minStationID = row[-2]
        maxStationID = row[-3]
        date = row[-4]
        seats = []
        seats.append(row[1])
        order.append(date)
        wagonNR.append(row[2])
        if row[-1] == 1:
            startStation = findMinStation(minStationID)
            endStation = findMaxStation(maxStationID)
            departureTime = findTime(row[-5], date, minStationID, 1, 0)
            arrivalTime = findTime(row[-5], date, maxStationID, 1, 1)
        else:
            startStation = findMaxStation(maxStationID)
            endStation = findMinStation(minStationID)
            arrivalTime = findTime(row[-5], date, minStationID, 1, 0)
            departureTime = findTime(row[-5], date, maxStationID, 1, 1)
        order.append(departureTime)
        order.append(arrivalTime)
        order.append(startStation)
        order.append(endStation)
        order.append(seats)
        order.append([])
        order.append([])
        order.append(wagonNR)
        orderDict[row[0]] = order
    else:
        order = orderDict[row[0]]
        order[-4].append(row[1])
        order[-1].append(row[2])
        orderDict[row[0]] = order

# Add information about cabin tickets to orders
for row in kupéBillettInfo:
    if row[0] not in orderDict.keys():
        order = []
        beds = []
        coupes = []
        seats = []
        wagonNR = []
        
        ruteID = row[1]
        dato = row[2]
        medHovedretning = row[3]
        coupes.append(row[4])
        beds.append(row[5])
        startStation = row[6]
        endStation = row[7]
        wagonNR.append(row[8])
    
        delstrekning1 = findDelstrekningID(startStation, medHovedretning, ruteID)
        delstrekning2 = findDelstrekningID(endStation, not medHovedretning, ruteID)

        if medHovedretning:
            departureTime = findTime(ruteID, dato, delstrekning1, medHovedretning, 0)
            arrivalTime = findTime(ruteID, dato, delstrekning2, medHovedretning, 1)
        else:
            departureTime = findTime(ruteID, dato, delstrekning2, medHovedretning, 1)
            arrivalTime = findTime(ruteID, dato, delstrekning1, medHovedretning, 0)

        order.append(dato)
        order.append(departureTime)
        order.append(arrivalTime)
        order.append(startStation)
        order.append(endStation)
        order.append(seats)
        order.append(beds)
        order.append(coupes)
        order.append(wagonNR)
        orderDict[row[0]] = order
    else:
        order = orderDict[row[0]]
        order[-3].append(row[5])
        order[-2].append(row[4])
        order[-1].append(row[8])
        orderDict[row[0]] = order

sorted_orderDict = dict(sorted(orderDict.items()))

# Make output for every order       
for key in sorted_orderDict.keys():
    orderList = orderDict[key]
    avgangsDato = orderList[0]
    avgangsTid = orderList[1]
    ankomstTid = orderList[2]
    startStasjon = orderList[3]
    sluttStasjon = orderList[4]
    sete = orderList[5]
    seng = orderList[6]
    kupe = orderList[7]
    vognNR = orderList[8]

    # Convert timestamps to datetime objects
    avgangsTid_dt = datetime.datetime.fromtimestamp(avgangsTid + avgangsDato)
    ankomstTid_dt = datetime.datetime.fromtimestamp(ankomstTid + avgangsDato)

    # Build result string
    result = f"Ordrenmmer:{key} Avreise: {avgangsTid_dt} {startStasjon} Ankomst: {ankomstTid_dt.time()} {sluttStasjon}"
    if len(sete) > 0:
        result += f" Sete(r): {sete}"
    if len(seng) > 0:
        result += f" Seng(er): {seng}"
    if len(kupe) > 0:
        result += f" i kupé(er): {kupe}"
    if len(wagonNR) > 0:
        result += f" i vogn(ene): {vognNR}"

    # Only print upcomimng orders. Order will be visible until you reach your destination
    if timeNow < ankomstTid + avgangsDato:
        print(result)
 
### Adding changes ###
connection.commit()
connection.close()
######################