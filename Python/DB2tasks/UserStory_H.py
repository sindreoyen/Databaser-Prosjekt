from lib2to3.pgen2.pgen import DFAState
import sqlite3
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

## Get out data from db
cursor.execute("""SELECT MAX(MAX(KjørerStrekning.tidStasjon1), MAX(KjørerStrekning.tidStasjon2)) as ankomst, MIN(MIN(KjørerStrekning.tidStasjon1), MIN(KjørerStrekning.tidStasjon2)) as avgang, Kundeordre.ordreNR, SetebillettIOrdre.seteNR, Togrute.ruteID, TogruteForekomst.dato, MAX(Delstrekning.delstrekningID) , MIN(Delstrekning.delstrekningID), Togrute.medHovedRetning
FROM Kundeordre
NATURAL Join Kunde
INNER JOIN TogruteForekomst USING (ruteID, dato)
NATURAL JOIN Togrute
NATURAL JOIN BillettIOrdre
NATURAL JOIN SetebillettIOrdre
NATURAL JOIN Delstrekning
NATURAL JOIN KjørerStrekning
WHERE Kunde.epost = ?
GROUP BY ordreNR, seteNR""", (email,))
times = cursor.fetchall()

#time
timeNow = int (time.time())
tidAvreise = times[0][-4] + times[0][1] + 3600*2

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

def findTime(ruteID, dato, delstrekningID, medHovedretning, typeStasjon):
    cursor.execute("""SELECT KjørerStrekning.tidStasjon1, KjørerStrekning.tidStasjon2
FROM TogruteForekomst
NATURAL JOIN KjørerStrekning
WHERE ruteID = ? AND dato = ? AND delstrekningID = ?""", (ruteID, dato, delstrekningID,))

    if medHovedretning:
        if typeStasjon == 0:
            return cursor.fetchall()[0][0]
        else:
            return cursor.fetchall()[0][1]
    else:
        if typeStasjon == 0:
            return cursor.fetchall()[0][1]
        else:
            return cursor.fetchall()[0][0]

## Make dict with all orders
orderDict = {}
for row in times:
    if row[2] not in orderDict.keys():
        order = []
        #departureTime = row[1]
        #arrivalTime = row[0]
        minStationID = row[-2]
        maxStationID = row[-3]
        date = row[-4]
        seats = []
        seats.append(row[3])
        order.append(date)
        #order.append(departureTime)
        #order.append(arrivalTime)
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
        orderDict[row[2]] = order
    else:
        order = orderDict[row[2]]
        order[-1].append(row[3])
        orderDict[row[2]] = order

for key in orderDict.keys():
    orderList = orderDict[key]
    avgangsDato = orderList[0]
    avgangsTid = orderList[1]
    ankomstTid = orderList[2]
    startStasjon = orderList[3]
    sluttStasjon = orderList[4]
    sete = orderList[5]
    if timeNow < ankomstTid + avgangsDato:
        print("Avreise:", datetime.datetime.fromtimestamp(avgangsTid + avgangsDato), startStasjon, "Ankomst:", datetime.datetime.fromtimestamp(ankomstTid + avgangsDato).time(), sluttStasjon, "Sete(r):", sete)
#Må fikse at ankomst ved midnatt blir good. 
### Adding changes ###
connection.commit()
connection.close()
######################