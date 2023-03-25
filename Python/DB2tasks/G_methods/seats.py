import sqlite3
import datetime

def orderSeat(connection: sqlite3.Connection, ids: list,
              startStation: str, endStation: str, 
              withMainDir: int, customerID: int):
    cursor = connection.cursor()

    ## Find available trains
    idx = 0
    trainMap = {}
    for id in ids:
        statement = """
        SELECT DATE(Tf.dato, 'unixepoch', 'localtime'), 
        KS.tidStasjon1, KS.tidStasjon2,
        Tf.navn, Tf.dato, Tf.ruteID
        FROM 
        Togruteforekomst Tf 
        LEFT OUTER NATURAL JOIN KjørerStrekning KS
        LEFT OUTER NATURAL JOIN Delstrekning Ds
        WHERE Tf.ruteID=?"""
        postfix = ("1" if withMainDir == 1 else "2")
        statement += " AND Ds.stasjon" + postfix + "='" + startStation + "'"
        statement += "\nORDER BY Tf.dato, KS.tidStasjon" + postfix + " DESC"

        for row in cursor.execute(statement, (id,)):
            if idx == 0:
                print("Velg ved å skrive inn nøkkelen til venstre, hvilken rute du ønsker:")
            trainMap[idx] = (row[5], row[3], row[4])
            startTime = datetime.datetime.utcfromtimestamp(row[1 if withMainDir else 2]).time()
            name = row[3]
            print("["+str(idx)+"]", row[0] + ": Tog", name, "går fra", startStation, "kl:", startTime)
            idx += 1
    key: int = -1
    if idx == 0:
        print("Ingen ledige togturer")
        return
    
    ## User chooses the desired departure
    while key not in trainMap.keys():
        key = int(input("Nøkkel: "))
    
    ## Find the available tickets for the trainride
    selected = trainMap[key]
    delstrekningIDs: list = fetchDelstrekningIDs(connection=connection,
                                           startStation=startStation, endStation=endStation,
                                           togruteID=selected[0], dir=withMainDir)
    
    ## Had to use f-strings to get the list of delstrekningIDs to work
    ## Finds all available seats for the chosen trainride
    statement = f"""
    SELECT Sete.seteNR, VognIOppsett.vognNR, ds.delstrekningID
    FROM
    Sete LEFT OUTER NATURAL JOIN
    Vogn LEFT OUTER NATURAL JOIN 
    VognIOppsett LEFT OUTER NATURAL JOIN
    VognOppsett LEFT NATURAL JOIN
    Togrute LEFT NATURAL JOIN
    TogruteForekomst Tf LEFT JOIN
    (SELECT * FROM Delstrekning WHERE delstrekningID IN ({str(delstrekningIDs)[1:-1]})) ds
    LEFT OUTER JOIN KundeOrdre ko ON ko.dato=Tf.dato AND ko.ruteID=Tf.ruteID
    LEFT OUTER NATURAL JOIN SetebillettIOrdre so
    WHERE Tf.ruteID=? AND Tf.navn=? AND Tf.dato=? AND so.billettID IS NULL
    ORDER BY Tf.dato, Sete.seteNR, VognIOppsett.vognNR ASC
    """
    allSeatsMap: dict = {}
    for row in cursor.execute(statement, (selected[0], selected[1], selected[2])):
        if row[2] in delstrekningIDs:
            key: str = str(row[0]) + "-" + str(row[1])
            try:
                allSeatsMap[key].append(row[2])
            except:
                allSeatsMap[key] = [row[2]]

    ## Let the user choose seats
    cartSeats: dict = {}
    for key in allSeatsMap:
        if allSeatsMap[key] == delstrekningIDs:
            seat = key.split("-")[0]
            cart = key.split("-")[1]
            try: cartSeats[cart].append(seat)
            except: cartSeats[cart] = [seat]
    
    if len(list(cartSeats.keys())) == 0:
        print("Det er dessverre ingen ledige seter...")
        return
    
    chosenCartSeats: dict = {}
    ordering: str = "y"
    while ordering.lower() == "y":
        if len(cartSeats.keys()) == 0:
            print("Det er dessverre ikke flere ledige seter på toget..")
        print("Det er ledige seter på toget! I vognene: " + str(list(cartSeats.keys())))
        # Pick cart
        cart = ""
        while cart not in cartSeats.keys():
            cart = input("Hvilken vogn ønsker du å sitte på?: ")
        # Pick seat
        print("Disse setene er ledige: " + str(list(cartSeats[cart])))
        seat = ""
        while seat not in cartSeats[cart]:
            seat = input("Hvilket sete ønsker du?: ")
        
        cartSeats[cart].remove(seat)
        if len(cartSeats[cart]) == 0:
            cartSeats.pop(cart)
        mylist: list = []
        print("Du har lagt til sete", seat, "i vogn", cart, "til din bestilling.")
        ordering = input("Skriv 'y' dersom du ønsker å legge til flere seter, trykk enter for å gå videre: ")
        try: chosenCartSeats[cart].append(seat)
        except: chosenCartSeats[cart] = [seat]
    createPurchase(delstrekningIDs=delstrekningIDs, chosenCartSeats=chosenCartSeats, customerID=customerID,
                   connection=connection, forekomst=selected)
  
### Send in purchase 
def createPurchase(delstrekningIDs: list, chosenCartSeats: dict, customerID: int,
                   connection: sqlite3.Connection, 
                   forekomst: tuple):
    cursor = connection.cursor()
    timestamp = int(datetime.datetime.now().timestamp())
    print("Legger inn din bestilling...")
    orderID = -1
    # Creating order
    try: 
        cursor.execute("INSERT INTO Kundeordre VALUES(NULL,?,?,?,?)",
                   (timestamp, customerID, forekomst[0], forekomst[2]))
        cursor.execute("""SELECT ko.ordreNR FROM
        Kundeordre ko WHERE ko.kjøpsTidspunkt=? AND ko.kundeID=?""", (timestamp, customerID))
        orderID = cursor.fetchone()[0]
    except: 
        print("Error i opprettelse av Kundeordre, prøv på nytt.")
        return

    ## Adding tickets to order
    for key in chosenCartSeats:
        for seat in chosenCartSeats[key]:
            cursor.execute("INSERT INTO Billett VALUES(NULL)")
            cursor.execute("SELECT * FROM Billett ORDER BY billettID DESC LIMIT 1")
            billettID = cursor.fetchone()[0]
            if (orderID != -1):
                cursor.execute("INSERT INTO BillettIOrdre VALUES(?,?)",(orderID, billettID))
            for delstrekning in delstrekningIDs:
                cursor.execute("INSERT INTO SetebillettIOrdre VALUES(?,?,?,?,?)",
                               (billettID, seat, key, delstrekning, orderID))
            print("Bekreftet bestilt: Sete nr", str(seat), "(" + "Vogn " + str(key) + ")")

    

###### Get Delstrekninger
def fetchDelstrekningIDs(connection: sqlite3.Connection,
                         startStation: str, endStation: str,
                         togruteID: int, dir: int) -> list:
    """Returns all the Delstrekning needed to cover a trip"""
    cursor = connection.cursor()
    hasStart = False
    hasEnd = False
    ids: list = []

    for row in cursor.execute("""
    SELECT ds.delstrekningID, ds.stasjon1, ds.stasjon2 
    FROM
    Togrute NATURAL JOIN 
    KjørerStrekning NATURAL JOIN Delstrekning ds
    WHERE Togrute.ruteID=?""", (togruteID,)):
        startIdx = 1 if dir == 1 else 2
        endIdx = 1 if startIdx == 2 else 2
        if row[startIdx] == startStation:
            hasStart = True
        if row[endIdx] == endStation:
            hasEnd = True
        if hasStart or hasEnd:
            ids.append(row[0])
        if hasStart and hasEnd:
            break
    return ids
