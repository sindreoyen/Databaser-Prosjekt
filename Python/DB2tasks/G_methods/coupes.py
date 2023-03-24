import sqlite3
import datetime

def orderCoupe(connection: sqlite3.Connection, ids: list,
              startStation: str, endStation: str, 
              withMainDir: int, customerID: int):
    
    cursor = connection.cursor()
    print("Coupe")
    ## Find available trains
    idx = 0
    trainMap = {}
    for id in ids:
        statement = """
        SELECT DATE(Tf.dato, 'unixepoch', 'localtime'), 
        KS.tidStasjon1, KS.tidStasjon2,
        Tf.navn, Tf.dato, Tf.ruteID, VognOppsett.oppsettID
        FROM 
        Togruteforekomst Tf LEFT OUTER NATURAL JOIN
        Togrute LEFT OUTER NATURAL JOIN
        VognOppsett LEFT OUTER NATURAL JOIN 
        VognIOppsett LEFT OUTER NATURAL JOIN
        Vogn LEFT OUTER NATURAL JOIN
        Sovevogn LEFT OUTER NATURAL JOIN
        KjørerStrekning KS LEFT OUTER NATURAL JOIN 
        Delstrekning Ds
        WHERE Tf.ruteID=? AND Sovevogn.vognID IS NOT NULL"""
        postfix = ("1" if withMainDir == 1 else "2")
        statement += " AND Ds.stasjon" + postfix + "='" + startStation + "'"
        statement += "\nORDER BY Tf.dato, KS.tidStasjon" + postfix + " DESC"

        for row in cursor.execute(statement, (id,)):
            if idx == 0:
                print("Velg ved å skrive inn nøkkelen til venstre, hvilken rute du ønsker:")
            trainMap[idx] = (row[5], row[3], row[4], row[6]) #forekomst info (id, navn, dato, oppsettID)
            startTime = datetime.datetime.utcfromtimestamp(row[1 if withMainDir else 2]).time()
            name = row[3]
            print("["+str(idx)+"]", row[0] + ": Tog", name, "går fra", startStation, "kl:", startTime)
            idx += 1
    coupe: int = -1
    if idx == 0:
        print("Ingen ledige togturer med kupé")
        return
    ## User chooses the desired departure
    while coupe not in trainMap.keys():
        coupe = int(input("Nøkkel: "))
    selected = trainMap[coupe]


    ## Find available coupes
    coupesMap: dict = {}
    wagon: int = -1
    wagonNR: int = -1
    statement = """
    SELECT Seng.sengNR, Sovekupe.kupeNR, Vogn.vognID, vio.vognNR FROM
    Vognoppsett vo LEFT OUTER NATURAL JOIN
    VognIOppsett vio LEFT OUTER NATURAL JOIN
    Vogn NATURAL JOIN
    Sovevogn LEFT OUTER NATURAL JOIN
    Sovekupe LEFT OUTER NATURAL JOIN 
    Seng LEFT OUTER JOIN HarKupeBillett b ON
    (b.vognID=Vogn.vognID AND b.kupeNR=Sovekupe.kupeNR 
    AND b.ruteID=? AND b.dato=?)
    WHERE vo.oppsettID=? AND b.billettID IS NULL
    """
    for row in cursor.execute(statement, (selected[0], selected[2], selected[3])):
        wagon = row[2]
        wagonNR = row[3]
        try: coupesMap[str(row[1])].append(str(row[0]))
        except: coupesMap[str(row[1])] = [str(row[0])]
    if wagon == -1: 
        print("Beklager, det er ingen ledige senger på dette toget.")
        return

    chosenCoupeBed: dict = {}
    ordering: str = "y"
    print("Det er kun én sovevogn på denne ruten.")
    while ordering.lower() == "y":
        if len(coupesMap.keys()) == 0:
            print("Det er ikke flere tilgjengelige senger på toget.")
            break
        print("Det er ledige senger på toget! I disse kupéene: " + str(list(coupesMap.keys())))
        # Pick coupe
        coupe = ""
        while coupe not in coupesMap.keys():
            coupe = input("Hvilken kupé ønsker du å sove i?: ")
        # Pick bed
        print("Disse sengene er ledige: " + str(list(coupesMap[coupe])))
        bed = ""
        while bed not in coupesMap[coupe]:
            bed = input("Hvilken seng ønsker du?: ")
        
        coupesMap[coupe].remove(bed)
        if len(coupesMap[coupe]) == 0:
            coupesMap.pop(coupe)
        mylist: list = []
        print("Du har lagt til seng", bed, "i kupé", coupe, "til din bestilling.")
        ordering = input("Skriv 'y' dersom du ønsker å legge til flere seter, trykk enter for å gå videre: ")
        try: chosenCoupeBed[coupe].append(bed)
        except: chosenCoupeBed[coupe] = [bed]
    createPurchase(chosenCoupeBeds=chosenCoupeBed, customerID=customerID,
                   connection=connection, forekomst=selected, wagon=wagon, wagonNR=wagonNR, startStation=startStation, endStation=endStation)

def createPurchase(chosenCoupeBeds: dict, customerID: int,
                   connection: sqlite3.Connection,
                   forekomst: tuple, wagon: int, wagonNR: int, startStation: str, endStation: str):
    cursor = connection.cursor()
    timestamp = int(datetime.datetime.now().timestamp())
    print("Legger inn din bestilling ...")
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
    for coupe in chosenCoupeBeds:
        for bed in chosenCoupeBeds[coupe]:
            cursor.execute("INSERT INTO Billett VALUES(NULL)")
            cursor.execute("SELECT * FROM Billett ORDER BY billettID DESC LIMIT 1")
            billettID = cursor.fetchone()[0]
            if (orderID != -1):
                cursor.execute("INSERT INTO BillettIOrdre VALUES(?,?)",(orderID, billettID))
            cursor.execute("INSERT INTO KupeBillett VALUES(?,?,?,?)", (billettID, coupe, bed, wagon))
            cursor.execute("INSERT INTO HarKupeBillett VALUES(?,?,?,?,?,?,?,?)",
                           (billettID, wagon, coupe, bed, forekomst[0], forekomst[2], startStation, endStation))
            print("Bekreftet bestilt: Seng nr", str(bed), "(" + "kupé nr. " + str(coupe) + ")"
                  + ", i vogn nr: " + str(wagonNR))