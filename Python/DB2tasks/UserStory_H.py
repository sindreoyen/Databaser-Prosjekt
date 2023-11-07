import LocalData
import Validators
import datetime

### Connecting to database #################
connection = LocalData.getDBConnection()
cursor = connection.cursor()
############################################


## Validate if epost exist in db
user: tuple = None
while user == None:
    email = input("Hei! Vennligst skriv eposten til brukeren du ønsker å sjekke reiser for: ")
    user = Validators.fetchUser(email=email, connection=connection)
    print("Her er dine fremtidige reiser:")

## User input for time and date, so that the code can be ran at any time
valid = False
while not valid:
    timestamp_str = input("Vennligst skriv inn tid på formatet: 'YYYY-MM-DD hh:mm': ") 
    
    try:
        userTime = datetime.datetime.strptime(timestamp_str, "%Y-%m-%d %H:%M")
        valid = True
    except ValueError:
        print("Formatet ble ikke korrekt. Vennligst prøv igjen.")

timeNow = int(userTime.timestamp())

## Extracting data from db about seat orders
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
GROUP BY ordreNR,vognNR, seteNR
ORDER BY ordreNR""", (email,))
seteBillettInfo = cursor.fetchall()

## Extracting data from db about cabin orders 
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
GROUP BY ordreNR, vognNR, kupeNR, sengNR
ORDER BY ordreNR""", (email,))

kupéBillettInfo = cursor.fetchall()

## Function for finding the correct delstrekningID from a stationName and routeID
def findDelstrekningID(stationName, medHovedretning, ruteID):
    """Returns the delstrekningID for a given stationName and routeID"""
    query = """SELECT delstrekningID
    FROM Delstrekning
    NATURAL JOIN KjørerStrekning """
    if medHovedretning:
        query += "WHERE Delstrekning.stasjon1 = ? AND ruteID = ?"
    else:
        query += "WHERE Delstrekning.stasjon2 = ? AND ruteID = ?"
    cursor.execute(query, (stationName, ruteID,))
    return cursor.fetchall()[0][0]


## Functions for finding the correct station
def findMinStation(stationID):
    """Returns the stationName for a given delstrekningID"""
    cursor.execute("""SELECT Delstrekning.stasjon1 
    FROM Delstrekning
    WHERE delstrekningID = ?""",(stationID,))
    station = cursor.fetchall()
    return station[0][0]

def findMaxStation(stationID):
    """Returns the stationName for a given delstrekningID"""
    cursor.execute("""SELECT Delstrekning.stasjon2 
    FROM Delstrekning
    WHERE delstrekningID = ?""",(stationID,))
    station = cursor.fetchall()
    return station[0][0]

## Function for finding the correct arrival/departure time for a selected station
def findTime(ruteID: int, dato: str, delstrekningID: int, medHovedretning: bool, typeStasjon: int) -> int:
    """Returns the arrival/departure time for a given station, route, date and direction"""
    query = "SELECT KjørerStrekning.tidStasjon1, KjørerStrekning.tidStasjon2 "
    query += "FROM TogruteForekomst NATURAL JOIN KjørerStrekning "
    query += "WHERE ruteID = ? AND dato = ? AND delstrekningID = ?"
    cursor.execute(query, (ruteID, dato, delstrekningID,))
    result = cursor.fetchall()[0]

    # Decide which time to return based on medHovedretning and typeStasjon parameters
    if medHovedretning:

        # Return arrival time if medHovedretning is True and typeStasjon is 0 or departure time if typeStasjon is 1
        return result[typeStasjon]
    else:

         # Return departure time if medHovedretning is False and typeStasjon is 0 or arrival time if typeStasjon is 1
        return result[1 - typeStasjon]

## Making a dict for all orders
orderDict = {}

## Adding information about seat tickets to orders
for row in seteBillettInfo:
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

## Add information about cabin tickets to orders
for row in kupéBillettInfo:
    if row[0] not in orderDict.keys():
        order = []
        beds = []
        cabins = []
        seats = []
        wagonNR = []
        
        ruteID = row[1]
        dato = row[2]
        medHovedretning = row[3]
        cabins.append(row[4])
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
        order.append(cabins)
        order.append(wagonNR)
        orderDict[row[0]] = order
    else:
        order = orderDict[row[0]]
        order[-3].append(row[5])
        order[-2].append(row[4])
        order[-1].append(row[8])
        orderDict[row[0]] = order

sorted_orderDict = dict(sorted(orderDict.items()))

## Make output for every order       
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

    ## The following code is mainly string formatting for presenting the tickets to the user 

    # Build result string
    result = f"Ordrenummer: {key} \n Avreisedato: {avgangsTid_dt.date()} \n Avgang: {avgangsTid_dt.time()} {startStasjon} \n Ankomst: {ankomstTid_dt.time()} {sluttStasjon}"

    # Make dictionarys for presenting seats and cabins with beds to the user in correct wagon
    ticketdict = {}
    seatdict = {}


    ## Statements for adding the correct seats, cabins and beds to their respective wagon

    # Only running if there are tickets in any wagons
    if len(vognNR) > 0:

        # Looping through the wagons
        for i in range(len(vognNR)):

            # Adding seats with vognNR as key if they are not in the seat dictionary
            if vognNR[i] not in seatdict:

                # Validating that there are elements in the sete list
                if len(sete) > 0:
                    seatdict[vognNR[i]] = [sete[i]]

            # Adding seats to the list if there are more seats in the same wagon
            else:
                 # Validating that there are elements in the sete list
                if len(sete) > 0:
                    seatdict[vognNR[i]].append(sete[i])

            # Doing the same, but this time for cabins and beds
            if vognNR[i] not in ticketdict:
                
                # Validating that there are elements in both kupe and seng lists
                if len(kupe) > 0 and len(seng) > 0:
                    cabindict = {}
                    cabindict[kupe[i]] = [seng[i]]
                    ticketdict[vognNR[i]] = cabindict
                elif len(seng) > 0:
                    ticketdict[vognNR[i]] = [seng[i]]

            else:

                # Validating that there are elements in both kupe and seng lists
                if len(kupe) > 0 and len(seng) > 0:
                    if kupe[i] not in ticketdict[vognNR[i]]:
                        ticketdict[vognNR[i]][kupe[i]] = [seng[i]]
                    else:
                        ticketdict[vognNR[i]][kupe[i]].append(seng[i])
    
    ## Adding the ordered tickets to the result string
    for key in seatdict:
        result += f"\n Sete(r): {seatdict[key]} i vogn {key}"
    
    for wagon in ticketdict:
        for cabin in ticketdict[wagon]:
            result += f"\n Seng(er): {ticketdict[wagon][cabin]}, i kupé {cabin}, vogn {wagon}"


    # Only print upcomimng orders. Order will be visible until you reach your destination
    if timeNow < ankomstTid + avgangsDato:
        print(result)
 
### Adding changes ###
connection.commit()
connection.close()
######################