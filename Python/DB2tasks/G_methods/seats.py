import sqlite3

def orderSeat(connection: sqlite3.Connection, ids: list,
              startStation: str, endStation: str, 
              withMainDir: int):
    cursor = connection.cursor()

    ## Find available trains
    idx = 0
    trainMap = {}
    for id in ids:
        statement = """
        SELECT DATE(Tf.dato, 'unixepoch', 'localtime'), 
        TIME(KS.tidStasjon1, 'unixepoch', 'localtime'), 
        TIME(KS.tidStasjon2, 'unixepoch', 'localtime'),
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
            startTime = row[1 if withMainDir else 2]
            name = row[3]
            print("["+str(idx)+"]", row[0] + ": Tog", name, "går fra", startStation, "kl:", startTime)
            idx += 1
    key: int = -1
    if idx == 0:
        print("Ingen ledige togturer")
        return
    
    while key not in trainMap.keys():
        key = int(input("Nøkkel: "))
    
    selected = trainMap[key]
    print("Selected trainride: ", selected)

    statement = """
    SELECT Sete.seteNR, VognIOppsett.vognNR, Tf.navn, Tf.ruteID,
    DATE(Tf.dato, 'unixepoch', 'localtime'), 
    ds.stasjon1, ds.stasjon2, ds.delstrekningID
    FROM
    Sete LEFT OUTER NATURAL JOIN
    Vogn LEFT NATURAL JOIN 
    VognIOppsett NATURAL JOIN
    VognOppsett LEFT OUTER NATURAL JOIN
    Togrute LEFT OUTER NATURAL JOIN
    TogruteForekomst Tf LEFT OUTER NATURAL JOIN
    Delstrekning ds
    WHERE Tf.ruteID=? AND Tf.navn=? AND Tf.dato=?
    ORDER BY Tf.dato, Sete.seteNR, VognIOppsett.vognNR ASC
    """
    allSeats: list = []
    for row in cursor.execute(statement, (selected[0], selected[1], selected[2])):
        print(row)